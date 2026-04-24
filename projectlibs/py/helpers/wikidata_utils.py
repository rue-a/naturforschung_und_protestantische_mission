# %%
import json
import time
from pathlib import Path

import requests

WIKIDATA_SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# Properties used for persons
PERSON_PROPERTIES = {
    "gnd": "P227",
    "factgrid": "P8168",
    "bionomia": "P6944",
    "saebi": "P1710",
}

# Properties used for locations
LOCATION_PROPERTIES = {
    "coordinates": "P625",
    "start": "P571",
    "end": "P576",
    "founder": "P112",
}

PERSON_SPARQL_QUERY = """\
SELECT ?gnd ?factgrid ?bionomia ?saebi WHERE {{
  BIND(wd:{qid} AS ?person)
  OPTIONAL {{ ?person wdt:P227  ?gnd. }}
  OPTIONAL {{ ?person wdt:P8168 ?factgrid. }}
  OPTIONAL {{ ?person wdt:P6944 ?bionomia. }}
  OPTIONAL {{ ?person wdt:P1710 ?saebi. }}
}}
"""

LOCATION_SPARQL_QUERY = """\
SELECT ?coordinates ?start ?end ?founderLabel WHERE {{
  BIND(wd:{qid} AS ?location)
  OPTIONAL {{ ?location wdt:P625 ?coordinates. }}
  OPTIONAL {{ ?location wdt:P571 ?start. }}
  OPTIONAL {{ ?location wdt:P576 ?end. }}
  OPTIONAL {{ ?location wdt:P112 ?founder.
              ?founder rdfs:label ?founderLabel.
              FILTER(LANG(?founderLabel) = "de" || LANG(?founderLabel) = "en") }}
}}
"""


# ── helpers ───────────────────────────────────────────────────────────────────


def extract_qid(wikidata_url_or_qid: str) -> str:
    """Return the bare QID from either 'Q12345' or a full Wikidata URL."""
    # e.g. https://www.wikidata.org/wiki/Q55874791  →  Q55874791
    return wikidata_url_or_qid.rstrip("/").rsplit("/", 1)[-1]


def _load_cache(cache_path: Path) -> dict:
    if cache_path.exists():
        with open(cache_path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_cache(cache: dict, cache_path: Path) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


# ── public API ────────────────────────────────────────────────────────────────


def fetch_person_data_from_wikipedia(
    wikidata_url_or_qid: str, cache_path: str, rewrite_cache: bool = False
) -> dict:
    """Query Wikidata for person identifier properties.

    Returns a flat dict ``{gnd, factgrid, bionomia, saebi}`` with ``None``
    for properties not present on the entity.  Results are persisted in the
    JSON cache at *cache_path* (keyed by QID) so each entity is only fetched
    once across runs.

    Network errors propagate as exceptions — callers should catch them and
    decide whether to skip enrichment for the affected record.
    """
    qid = extract_qid(wikidata_url_or_qid)
    cache_path = Path(cache_path)

    cache = _load_cache(cache_path)
    if qid in cache and not rewrite_cache:
        print("using cached data for enrichment")
        return cache[qid]

    query = PERSON_SPARQL_QUERY.format(qid=qid)
    response = requests.get(
        WIKIDATA_SPARQL_ENDPOINT,
        params={"query": query, "format": "json"},
        headers={"User-Agent": "naturforschung-mission-bot/1.0 (research project)"},
        timeout=30,
    )
    response.raise_for_status()

    bindings = response.json()["results"]["bindings"]

    # OPTIONAL triples can produce multiple rows when a property has several
    # values.  Collect the first non-None value for each key.
    result = {key: None for key in PERSON_PROPERTIES}
    for row in bindings:
        for key in PERSON_PROPERTIES:
            if result[key] is None and key in row:
                result[key] = row[key]["value"]

    cache[qid] = result
    _save_cache(cache, cache_path)

    time.sleep(0.5)  # stay within Wikidata rate limits
    return result


# fetch_person_data_from_wikipedia(
#     "https://www.wikidata.org/wiki/Q62241",
#     "../../../data/cache_persons_wikidata.json",
# )


def _parse_wkt_point(wkt: str) -> dict | None:
    """Parse a WKT Point string into ``{lat, lon}``.

    Wikidata returns coordinates as e.g. ``Point(8.55 47.3666)`` (lon lat order).
    Returns ``None`` if parsing fails.
    """
    try:
        inner = wkt.strip().removeprefix("Point(").removesuffix(")")
        lon_str, lat_str = inner.split()
        return {"lat": float(lat_str), "lon": float(lon_str)}
    except Exception:
        return None


def fetch_location_data_from_wikidata(
    wikidata_url_or_qid: str, cache_path: str, rewrite_cache: bool = False
) -> dict:
    """Query Wikidata for location properties.

    Returns a dict ``{coordinates: {lat, lon} | None, start, end, founder}``
    with ``None`` for absent properties.  Results are cached in *cache_path*
    (JSON, keyed by QID).

    When the founder has labels in both German and English the German label
    takes preference.
    """
    qid = extract_qid(wikidata_url_or_qid)
    cache_path = Path(cache_path)

    cache = _load_cache(cache_path)
    if qid in cache and not rewrite_cache:
        print("using cached data for enrichment")
        return cache[qid]

    query = LOCATION_SPARQL_QUERY.format(qid=qid)
    response = requests.get(
        WIKIDATA_SPARQL_ENDPOINT,
        params={"query": query, "format": "json"},
        headers={"User-Agent": "naturforschung-mission-bot/1.0 (research project)"},
        timeout=30,
    )
    response.raise_for_status()

    bindings = response.json()["results"]["bindings"]

    result = {"coordinates": None, "start": None, "end": None, "founder": None}
    for row in bindings:
        if result["coordinates"] is None and "coordinates" in row:
            result["coordinates"] = _parse_wkt_point(row["coordinates"]["value"])
        if result["start"] is None and "start" in row:
            result["start"] = row["start"]["value"]
        if result["end"] is None and "end" in row:
            result["end"] = row["end"]["value"]
        # Prefer German founder label over English
        if "founderLabel" in row:
            lang = row["founderLabel"].get("xml:lang", "")
            if result["founder"] is None or lang == "de":
                result["founder"] = row["founderLabel"]["value"]

    cache[qid] = result
    _save_cache(cache, Path(cache_path))

    time.sleep(0.5)  # stay within Wikidata rate limits
    return result


# fetch_location_data_from_wikidata(
#     "https://www.wikidata.org/wiki/Q423740",
#     "../../../data/cache_locations_wikidata.json",
# )

# %%
