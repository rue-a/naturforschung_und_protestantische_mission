import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError

from projectlibs.py.enrich_utils import (
    extract_url_field,
    fetch_json,
    load_json,
    make_decimal_field,
    make_list_field,
    make_string_field,
    make_url_field,
)


WIKIDATA_QID_RE = re.compile(r"/wiki/(Q\d+)$")
DEFAULT_LOCATIONS_CACHE = Path("data/wikidata_locations_cache.json")
DEFAULT_PERSONS_CACHE = Path("data/wikidata_persons_cache.json")
USER_AGENT = "naturforschung-und-protestantische-mission/1.0 (wikidata enrichment)"

WIKIDATA_PROPERTIES = {
    "gnd": "P227",
    "factgrid": "P8168",
    "bionomia": "P6944",
    "saebi": "P1710",
    "inception": "P571",
    "founder": "P112",
    "dissolved_abolished_or_demolished_date": "P576",
}


def fetch_wikidata_entity(qid: str) -> dict[str, Any]:
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    return fetch_json(url, user_agent=USER_AGENT)


def fetch_wikidata_entity_labels(qids: list[str]) -> dict[str, str]:
    if not qids:
        return {}

    unique_qids = sorted(set(qids))
    ids = "|".join(unique_qids)
    url = (
        "https://www.wikidata.org/w/api.php"
        f"?action=wbgetentities&format=json&props=labels&languages=de|en&ids={ids}"
    )
    payload = fetch_json(url, user_agent=USER_AGENT)
    entities = payload.get("entities", {})
    labels = {}

    for qid in unique_qids:
        entity = entities.get(qid, {})
        entity_labels = entity.get("labels", {})

        if "de" in entity_labels:
            labels[qid] = entity_labels["de"]["value"]
            continue
        if "en" in entity_labels:
            labels[qid] = entity_labels["en"]["value"]
            continue

        labels[qid] = qid

    return labels


def extract_claim_string(entity_payload: dict[str, Any], qid: str, property_id: str) -> str | None:
    entity = entity_payload.get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    for claim in claims.get(property_id, []):
        datavalue = claim.get("mainsnak", {}).get("datavalue", {})
        value = datavalue.get("value")
        if isinstance(value, str) and value:
            return value

    return None


def extract_claim_entity_ids(
    entity_payload: dict[str, Any],
    qid: str,
    property_id: str,
) -> list[str]:
    entity = entity_payload.get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})
    entity_ids = []

    for claim in claims.get(property_id, []):
        datavalue = claim.get("mainsnak", {}).get("datavalue", {})
        value = datavalue.get("value", {})
        entity_id = value.get("id")
        if entity_id:
            entity_ids.append(entity_id)

    return entity_ids


def format_wikidata_time(value: dict[str, Any]) -> str | None:
    raw_time = value.get("time")
    if not raw_time:
        return None

    match = re.match(r"([+-])(\d+)-(\d{2})-(\d{2})T", raw_time)
    if not match:
        return raw_time

    sign, year, month, day = match.groups()
    precision = value.get("precision", 9)
    normalized_year = year.lstrip("0") or "0"
    if sign == "-":
        normalized_year = f"-{normalized_year}"

    if precision >= 11 and month != "00" and day != "00":
        return f"{normalized_year}-{month}-{day}"
    if precision >= 10 and month != "00":
        return f"{normalized_year}-{month}"
    return normalized_year


def extract_claim_time(entity_payload: dict[str, Any], qid: str, property_id: str) -> str | None:
    entity = entity_payload.get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    for claim in claims.get(property_id, []):
        datavalue = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if not datavalue:
            continue

        formatted_time = format_wikidata_time(datavalue)
        if formatted_time:
            return formatted_time

    return None


def extract_coordinates(entity_payload: dict[str, Any], qid: str) -> tuple[float, float] | None:
    entity = entity_payload.get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    for claim in claims.get("P625", []):
        datavalue = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
        if not datavalue:
            continue

        latitude = datavalue.get("latitude")
        longitude = datavalue.get("longitude")

        if latitude is None or longitude is None:
            continue

        return float(longitude), float(latitude)

    return None


def extract_wikidata_qid_from_links_list(record: dict[str, Any]) -> str | None:
    links_field = record.get("links")
    if not links_field:
        return None

    value = links_field.get("value", {})
    if value.get("type") != "List":
        return None

    for item in value.get("value", []):
        if item.get("type") != "URL":
            continue

        match = WIKIDATA_QID_RE.search(item.get("value", ""))
        if match:
            return match.group(1)

    return None


def extract_wikidata_qid_from_person_links(record: dict[str, Any]) -> str | None:
    links = record.get("links")
    if not isinstance(links, dict):
        return None

    wikidata_url = extract_url_field(links.get("wikidata"))
    if not wikidata_url:
        return None

    match = WIKIDATA_QID_RE.search(wikidata_url)
    if match:
        return match.group(1)

    return None


def load_wikidata_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return load_json(path)


def ensure_person_links_container(record: dict[str, Any]) -> dict[str, Any]:
    links = record.setdefault("links", {})
    if not isinstance(links, dict):
        raise TypeError("Person links field must be an object")
    return links


def build_person_link_urls(qid: str, entity_payload: dict[str, Any]) -> dict[str, str]:
    urls = {}

    gnd_id = extract_claim_string(entity_payload, qid, WIKIDATA_PROPERTIES["gnd"])
    if gnd_id:
        urls["gnd"] = f"https://d-nb.info/gnd/{gnd_id}"

    factgrid_id = extract_claim_string(entity_payload, qid, WIKIDATA_PROPERTIES["factgrid"])
    if factgrid_id:
        urls["factgrid"] = f"https://database.factgrid.de/wiki/Item:{factgrid_id}"

    bionomia_id = extract_claim_string(entity_payload, qid, WIKIDATA_PROPERTIES["bionomia"])
    if bionomia_id:
        urls["bionomia"] = f"https://bionomia.net/{bionomia_id}"
    else:
        urls["bionomia"] = f"https://bionomia.net/{qid}"

    saebi_id = extract_claim_string(entity_payload, qid, WIKIDATA_PROPERTIES["saebi"])
    if saebi_id:
        urls["saebi"] = f"https://saebi.isgv.de/gnd/{saebi_id}"

    return urls


def build_location_enrichment(entity_payload: dict[str, Any], qid: str) -> dict[str, Any]:
    coordinates = extract_coordinates(entity_payload, qid)
    founder_ids = extract_claim_entity_ids(entity_payload, qid, WIKIDATA_PROPERTIES["founder"])
    referenced_entity_labels = fetch_wikidata_entity_labels(founder_ids)

    return {
        "coordinates": (
            {
                "longitude": coordinates[0],
                "latitude": coordinates[1],
            }
            if coordinates
            else None
        ),
        "inception": extract_claim_time(entity_payload, qid, WIKIDATA_PROPERTIES["inception"]),
        "founder": [referenced_entity_labels[entity_id] for entity_id in founder_ids],
        "dissolved_abolished_or_demolished_date": extract_claim_time(
            entity_payload,
            qid,
            WIKIDATA_PROPERTIES["dissolved_abolished_or_demolished_date"],
        ),
    }


def normalize_location_lookup_entry(entry: Any) -> dict[str, Any]:
    if entry is None:
        return {
            "coordinates": None,
            "inception": None,
            "founder": [],
            "dissolved_abolished_or_demolished_date": None,
        }

    if "coordinates" in entry:
        return entry

    coordinates = None
    if "longitude" in entry and "latitude" in entry:
        coordinates = {
            "longitude": entry["longitude"],
            "latitude": entry["latitude"],
        }

    return {
        "coordinates": coordinates,
        "inception": entry.get("inception"),
        "founder": entry.get("founder", []),
        "dissolved_abolished_or_demolished_date": entry.get(
            "dissolved_abolished_or_demolished_date"
        ),
    }


def apply_location_enrichment(
    record: dict[str, Any],
    enrichment: dict[str, Any],
    *,
    overwrite: bool,
) -> list[str]:
    enriched_fields = []

    coordinates = enrichment["coordinates"]
    if coordinates:
        if overwrite or "longitude" not in record:
            record["longitude"] = make_decimal_field("Longitude", coordinates["longitude"])
            enriched_fields.append("longitude")
        if overwrite or "latitude" not in record:
            record["latitude"] = make_decimal_field("Latitude", coordinates["latitude"])
            enriched_fields.append("latitude")

    if enrichment["inception"] and (overwrite or "inception" not in record):
        record["inception"] = make_string_field(
            "Inception",
            enrichment["inception"],
            type_name="ISO8601_2_Date",
        )
        enriched_fields.append("inception")

    if enrichment["founder"] and (overwrite or "founder" not in record):
        record["founder"] = make_list_field("Founder", enrichment["founder"])
        enriched_fields.append("founder")

    if (
        enrichment["dissolved_abolished_or_demolished_date"]
        and (overwrite or "dissolved_abolished_or_demolished_date" not in record)
    ):
        record["dissolved_abolished_or_demolished_date"] = make_string_field(
            "Dissolved, abolished or demolished date",
            enrichment["dissolved_abolished_or_demolished_date"],
            type_name="ISO8601_2_Date",
        )
        enriched_fields.append("dissolved_abolished_or_demolished_date")

    return enriched_fields


def enrich_locations(
    payload: dict[str, Any],
    locations_cache: dict[str, Any],
    *,
    overwrite: bool = False,
    refresh_cache: bool = False,
    pause_seconds: float = 0.1,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, int]]:
    updated = 0
    skipped = 0
    failed = 0

    for location_id, record in payload.items():
        qid = extract_wikidata_qid_from_links_list(record)
        if not qid:
            skipped += 1
            print(f"[locations] skipped {location_id}: no Wikidata QID")
            continue

        if not refresh_cache and qid in locations_cache:
            enrichment = normalize_location_lookup_entry(locations_cache[qid])
        else:
            try:
                entity_payload = fetch_wikidata_entity(qid)
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
                failed += 1
                print(f"[locations] failed {location_id} from {qid}: could not fetch Wikidata entity")
                continue

            enrichment = build_location_enrichment(entity_payload, qid)
            locations_cache[qid] = enrichment

        enriched_fields = apply_location_enrichment(
            record,
            enrichment,
            overwrite=overwrite,
        )

        if not enriched_fields:
            skipped += 1
            print(f"[locations] skipped {location_id} from {qid}: no new fields to add")
            continue

        updated += 1
        print(
            f"[locations] enriched {location_id} from {qid}: added {', '.join(enriched_fields)}"
        )

        if pause_seconds:
            time.sleep(pause_seconds)

    return payload, locations_cache, {
        "updated": updated,
        "skipped": skipped,
        "failed": failed,
    }


def enrich_person_links(
    payload: dict[str, Any],
    persons_cache: dict[str, Any],
    *,
    overwrite: bool = False,
    refresh_cache: bool = False,
    pause_seconds: float = 0.1,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, int]]:
    updated = 0
    skipped = 0
    failed = 0

    labels = {
        "gnd": "Links - GND",
        "factgrid": "Links - FactGrid",
        "bionomia": "Links - Bionomia",
        "saebi": "Links - Säbi",
    }

    for person_id, record in payload.items():
        qid = extract_wikidata_qid_from_person_links(record)
        if not qid:
            skipped += 1
            print(f"[persons] skipped {person_id}: no Wikidata QID")
            continue

        links = ensure_person_links_container(record)
        missing_targets = [key for key in labels if overwrite or key not in links]

        if not missing_targets:
            skipped += 1
            print(f"[persons] skipped {person_id} from {qid}: no missing link fields")
            continue

        if not refresh_cache and qid in persons_cache:
            entity_payload = persons_cache[qid]
        else:
            try:
                entity_payload = fetch_wikidata_entity(qid)
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
                failed += 1
                print(f"[persons] failed {person_id} from {qid}: could not fetch Wikidata entity")
                continue
            persons_cache[qid] = entity_payload

        candidate_urls = build_person_link_urls(qid, entity_payload)
        changed = False
        enriched_fields = []

        for key in missing_targets:
            url = candidate_urls.get(key)
            if not url:
                continue

            links[key] = make_url_field(labels[key], url)
            changed = True
            enriched_fields.append(key)

        if changed:
            updated += 1
            print(
                f"[persons] enriched {person_id} from {qid}: added {', '.join(enriched_fields)}"
            )
        else:
            skipped += 1
            print(f"[persons] skipped {person_id} from {qid}: no usable Wikidata links found")

        if pause_seconds:
            time.sleep(pause_seconds)

    return payload, persons_cache, {
        "updated": updated,
        "skipped": skipped,
        "failed": failed,
    }
