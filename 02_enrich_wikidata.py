import argparse
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError

from enrich_utils import (
    extract_url_field,
    fetch_json,
    load_json,
    make_decimal_field,
    make_url_field,
    save_json,
)


WIKIDATA_QID_RE = re.compile(r"/wiki/(Q\d+)$")
DEFAULT_LOCATIONS_INPUT = Path("data/locations.json")
DEFAULT_PERSONS_INPUT = Path("data/persons.json")
USER_AGENT = "naturforschung-und-protestantische-mission/1.0 (wikidata enrichment)"

WIKIDATA_PROPERTIES = {
    "gnd": "P227",
    "factgrid": "P8168",
    "bionomia": "P6944",
    "saebi": "P1710",
}

def fetch_wikidata_entity(qid: str) -> dict[str, Any]:
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    return fetch_json(url, user_agent=USER_AGENT)


def extract_claim_string(entity_payload: dict[str, Any], qid: str, property_id: str) -> str | None:
    entity = entity_payload.get("entities", {}).get(qid, {})
    claims = entity.get("claims", {})

    for claim in claims.get(property_id, []):
        datavalue = claim.get("mainsnak", {}).get("datavalue", {})
        value = datavalue.get("value")
        if isinstance(value, str) and value:
            return value

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
        # In existing data, Bionomia links often mirror the Wikidata QID.
        urls["bionomia"] = f"https://bionomia.net/{qid}"

    saebi_id = extract_claim_string(entity_payload, qid, WIKIDATA_PROPERTIES["saebi"])
    if saebi_id:
        urls["saebi"] = f"https://saebi.isgv.de/gnd/{saebi_id}"

    return urls


def enrich_locations(
    payload: dict[str, Any],
    *,
    overwrite: bool = False,
    pause_seconds: float = 0.1,
) -> tuple[dict[str, Any], dict[str, int]]:
    updated = 0
    skipped = 0
    failed = 0

    for location_id, record in payload.items():
        has_longitude = "longitude" in record
        has_latitude = "latitude" in record

        if not overwrite and has_longitude and has_latitude:
            skipped += 1
            continue

        qid = extract_wikidata_qid_from_links_list(record)
        if not qid:
            skipped += 1
            continue

        try:
            entity_payload = fetch_wikidata_entity(qid)
            coordinates = extract_coordinates(entity_payload, qid)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            failed += 1
            continue

        if not coordinates:
            skipped += 1
            continue

        longitude, latitude = coordinates
        record["longitude"] = make_decimal_field("Longitude", longitude)
        record["latitude"] = make_decimal_field("Latitude", latitude)
        updated += 1
        print(
            f"[locations] enriched {location_id} from {qid}: longitude={longitude}, latitude={latitude}"
        )

        if pause_seconds:
            time.sleep(pause_seconds)

    return payload, {
        "updated": updated,
        "skipped": skipped,
        "failed": failed,
    }


def enrich_person_links(
    payload: dict[str, Any],
    *,
    overwrite: bool = False,
    pause_seconds: float = 0.1,
) -> tuple[dict[str, Any], dict[str, int]]:
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
            continue

        links = ensure_person_links_container(record)
        missing_targets = [
            key for key in labels
            if overwrite or key not in links
        ]

        if not missing_targets:
            skipped += 1
            continue

        try:
            entity_payload = fetch_wikidata_entity(qid)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            failed += 1
            continue

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

        if pause_seconds:
            time.sleep(pause_seconds)

    return payload, {
        "updated": updated,
        "skipped": skipped,
        "failed": failed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich project JSON data from linked Wikidata entities."
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing values.",
    )
    parser.add_argument(
        "--pause-seconds",
        type=float,
        default=0.1,
        help="Pause between Wikidata requests.",
    )
    args = parser.parse_args()

    locations_input = DEFAULT_LOCATIONS_INPUT
    persons_input = DEFAULT_PERSONS_INPUT
    locations_output = locations_input
    persons_output = persons_input

    locations_payload = load_json(locations_input)
    enriched_locations, location_stats = enrich_locations(
        locations_payload,
        overwrite=args.overwrite,
        pause_seconds=args.pause_seconds,
    )
    save_json(locations_output, enriched_locations)

    persons_payload = load_json(persons_input)
    enriched_persons, person_stats = enrich_person_links(
        persons_payload,
        overwrite=args.overwrite,
        pause_seconds=args.pause_seconds,
    )
    save_json(persons_output, enriched_persons)

    print("Finished.")
    print(
        f"locations: updated={location_stats['updated']} skipped={location_stats['skipped']} failed={location_stats['failed']} output={locations_output}"
    )
    print(
        f"persons: updated={person_stats['updated']} skipped={person_stats['skipped']} failed={person_stats['failed']} output={persons_output}"
    )


if __name__ == "__main__":
    main()
