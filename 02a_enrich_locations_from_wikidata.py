import argparse
from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.wikidata_enrichment import (
    DEFAULT_LOCATIONS_CACHE,
    enrich_locations,
    load_wikidata_cache,
)


DEFAULT_INPUT = Path("data/locations.json")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich locations JSON with coordinates and metadata from Wikidata."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Input locations JSON file.",
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
    parser.add_argument(
        "--locations-cache",
        type=Path,
        default=DEFAULT_LOCATIONS_CACHE,
        help="Path to the Wikidata locations cache file.",
    )
    parser.add_argument(
        "--refresh-locations-cache",
        action="store_true",
        help="Ignore the existing Wikidata locations cache and refresh it from Wikidata.",
    )
    args = parser.parse_args()

    print("Enriching locations from Wikidata...")
    print(f"input: {args.input}")
    print(f"locations cache: {args.locations_cache}")
    print(f"overwrite existing values: {args.overwrite}")
    print(f"refresh locations cache: {args.refresh_locations_cache}")

    print("Loading locations JSON...")
    payload = load_json(args.input)
    print("Loading locations cache...")
    locations_cache = load_wikidata_cache(args.locations_cache)

    print("Running Wikidata enrichment for locations...")
    enriched_payload, locations_cache, stats = enrich_locations(
        payload,
        locations_cache,
        overwrite=args.overwrite,
        refresh_cache=args.refresh_locations_cache,
        pause_seconds=args.pause_seconds,
    )
    print("Writing enriched locations JSON...")
    save_json(args.input, enriched_payload)
    print("Writing locations cache...")
    save_json(args.locations_cache, locations_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {args.input}")
    print(f"locations cache: {args.locations_cache}")


if __name__ == "__main__":
    main()
