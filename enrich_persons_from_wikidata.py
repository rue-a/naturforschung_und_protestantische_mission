from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.wikidata_enrichment import (
    enrich_person_links,
    load_wikidata_cache,
)


DEFAULT_INPUT = Path("data/persons.json")
OVERWRITE = False
PAUSE_SECONDS = 0.1
PERSONS_CACHE = Path("data/wikidata_persons_cache.json")
REFRESH_PERSONS_CACHE = False


def main() -> None:
    print()
    print("Running enrich_persons_from_wikidata.py")
    print("Enriching persons from Wikidata...")
    print(f"input: {DEFAULT_INPUT}")
    print(f"persons cache: {PERSONS_CACHE}")
    print(f"overwrite existing values: {OVERWRITE}")
    print(f"refresh persons cache: {REFRESH_PERSONS_CACHE}")

    print("Loading persons JSON...")
    payload = load_json(DEFAULT_INPUT)
    print("Loading persons cache...")
    persons_cache = load_wikidata_cache(PERSONS_CACHE)

    print("Running Wikidata enrichment for persons...")
    enriched_payload, persons_cache, stats = enrich_person_links(
        payload,
        persons_cache,
        overwrite=OVERWRITE,
        refresh_cache=REFRESH_PERSONS_CACHE,
        pause_seconds=PAUSE_SECONDS,
    )
    print("Writing enriched persons JSON...")
    save_json(DEFAULT_INPUT, enriched_payload)
    print("Writing persons cache...")
    save_json(PERSONS_CACHE, persons_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {DEFAULT_INPUT}")
    print(f"persons cache: {PERSONS_CACHE}")


if __name__ == "__main__":
    main()
