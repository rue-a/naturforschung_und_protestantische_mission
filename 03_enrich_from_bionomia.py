import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError

from enrich_utils import (
    extract_url_field,
    fetch_json,
    load_json,
    make_object_field,
    save_json,
)


DEFAULT_INPUT = Path("data/persons.wikidata.enriched.json")
DEFAULT_OUTPUT = Path("data/persons.wikidata.bionomia.enriched.json")
USER_AGENT = "naturforschung-und-protestantische-mission/1.0 (bionomia enrichment)"

BIONOMIA_QID_RE = re.compile(r"bionomia\.net/(?:[a-z]{2}/)?(Q\d+)$")
def extract_qid_from_person(record: dict[str, Any]) -> str | None:
    links = record.get("links", {})
    if not isinstance(links, dict):
        return None

    bionomia_url = extract_url_field(links.get("bionomia"))
    if bionomia_url:
        match = BIONOMIA_QID_RE.search(bionomia_url)
        if match:
            return match.group(1)

    return None


def bionomia_profile_url(qid: str) -> str:
    return f"https://bionomia.net/{qid}"


def bionomia_api_url(qid: str) -> str:
    return f"https://api.bionomia.net/{qid}.jsonld"


def pick_first_string(data: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def normalize_same_as(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def normalize_bionomia_profile(profile: dict[str, Any], qid: str) -> dict[str, Any]:
    normalized = {
        "qid": qid,
        "api_url": bionomia_api_url(qid),
        "profile_url": bionomia_profile_url(qid),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "raw_jsonld": profile,
    }

    profile_id = pick_first_string(profile, "@id", "id")
    if profile_id:
        normalized["profile_id"] = profile_id

    name = pick_first_string(profile, "name", "label")
    if name:
        normalized["name"] = name

    description = profile.get("description")
    if isinstance(description, str) and description:
        normalized["description"] = description

    same_as = normalize_same_as(profile.get("sameAs"))
    if same_as:
        normalized["same_as"] = same_as

    identifiers = {}
    for url in same_as:
        if "wikidata.org/wiki/" in url:
            identifiers["wikidata"] = url
        elif "d-nb.info/gnd/" in url:
            identifiers["gnd"] = url
        elif "orcid.org/" in url:
            identifiers["orcid"] = url
    if identifiers:
        normalized["identifiers"] = identifiers

    return normalized


def enrich_persons_from_bionomia(
    payload: dict[str, Any],
    *,
    overwrite: bool = False,
    pause_seconds: float = 0.1,
) -> tuple[dict[str, Any], dict[str, int]]:
    updated = 0
    skipped = 0
    failed = 0

    for _, record in payload.items():
        qid = extract_qid_from_person(record)
        if not qid:
            skipped += 1
            continue

        enrichment = record.setdefault("enrichment", {})
        has_bionomia_enrichment = "bionomia" in enrichment
        if has_bionomia_enrichment and not overwrite:
            skipped += 1
            continue

        try:
            profile = fetch_json(
                bionomia_api_url(qid),
                user_agent=USER_AGENT,
                accept="application/ld+json, application/json",
            )
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            failed += 1
            continue

        enrichment = record.setdefault("enrichment", {})
        enrichment["bionomia"] = make_object_field(
            "Enrichment - Bionomia",
            normalize_bionomia_profile(profile, qid),
        )
        updated += 1

        if pause_seconds:
            time.sleep(pause_seconds)

    return payload, {
        "updated": updated,
        "skipped": skipped,
        "failed": failed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich persons JSON with profile data from Bionomia."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Input persons JSON file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output file for enriched persons JSON.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing Bionomia enrichment.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Write the enriched data back to the input file.",
    )
    parser.add_argument(
        "--pause-seconds",
        type=float,
        default=0.1,
        help="Pause between requests.",
    )
    args = parser.parse_args()

    output_path = args.input if args.in_place else args.output
    payload = load_json(args.input)
    enriched_payload, stats = enrich_persons_from_bionomia(
        payload,
        overwrite=args.overwrite,
        pause_seconds=args.pause_seconds,
    )
    save_json(output_path, enriched_payload)

    print(
        f"Finished. updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']} output={output_path}"
    )


if __name__ == "__main__":
    main()
