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


def main(
    input_path: Path = DEFAULT_INPUT,
    overwrite: bool = OVERWRITE,
    pause_seconds: float = PAUSE_SECONDS,
    locations_cache_path: Path = LOCATIONS_CACHE,
    refresh_locations_cache: bool = REFRESH_LOCATIONS_CACHE,
) -> None:
    print("Enriching locations from Wikidata...")
    print(f"input: {input_path}")
    print(f"locations cache: {locations_cache_path}")
    print(f"overwrite existing values: {overwrite}")
    print(f"refresh locations cache: {refresh_locations_cache}")

    print("Loading locations JSON...")
    payload = load_json(input_path)
    print("Loading locations cache...")
    locations_cache = load_wikidata_cache(locations_cache_path)

    print("Running Wikidata enrichment for locations...")
    enriched_payload, locations_cache, stats = enrich_locations(
        payload,
        locations_cache,
        overwrite=overwrite,
        refresh_cache=refresh_locations_cache,
        pause_seconds=pause_seconds,
    )
    print("Writing enriched locations JSON...")
    save_json(input_path, enriched_payload)
    print("Writing locations cache...")
    save_json(locations_cache_path, locations_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {input_path}")
    print(f"locations cache: {locations_cache_path}")


if __name__ == "__main__":
    main()
