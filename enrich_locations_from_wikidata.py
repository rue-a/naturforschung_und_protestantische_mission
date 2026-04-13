from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.wikidata_enrichment import (
    enrich_locations,
    load_wikidata_cache,
)


DEFAULT_INPUT = Path("data/locations.json")
OVERWRITE = False
PAUSE_SECONDS = 0.1
LOCATIONS_CACHE = Path("data/wikidata_locations_cache.json")
REFRESH_LOCATIONS_CACHE = False


def main() -> None:
    print()
    print("Running enrich_locations_from_wikidata.py")
    print("Enriching locations from Wikidata...")
    print(f"input: {DEFAULT_INPUT}")
    print(f"locations cache: {LOCATIONS_CACHE}")
    print(f"overwrite existing values: {OVERWRITE}")
    print(f"refresh locations cache: {REFRESH_LOCATIONS_CACHE}")

    print("Loading locations JSON...")
    payload = load_json(DEFAULT_INPUT)
    print("Loading locations cache...")
    locations_cache = load_wikidata_cache(LOCATIONS_CACHE)

    print("Running Wikidata enrichment for locations...")
    enriched_payload, locations_cache, stats = enrich_locations(
        payload,
        locations_cache,
        overwrite=OVERWRITE,
        refresh_cache=REFRESH_LOCATIONS_CACHE,
        pause_seconds=PAUSE_SECONDS,
    )
    print("Writing enriched locations JSON...")
    save_json(DEFAULT_INPUT, enriched_payload)
    print("Writing locations cache...")
    save_json(LOCATIONS_CACHE, locations_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {DEFAULT_INPUT}")
    print(f"locations cache: {LOCATIONS_CACHE}")


if __name__ == "__main__":
    main()
