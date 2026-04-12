import argparse
from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.wikidata_enrichment import (
    DEFAULT_PERSONS_CACHE,
    enrich_person_links,
    load_wikidata_cache,
)


DEFAULT_INPUT = Path("data/persons.json")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enrich persons JSON with external links from Wikidata."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Input persons JSON file.",
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
        "--persons-cache",
        type=Path,
        default=DEFAULT_PERSONS_CACHE,
        help="Path to the Wikidata persons cache file.",
    )
    parser.add_argument(
        "--refresh-persons-cache",
        action="store_true",
        help="Ignore the existing Wikidata persons cache and refresh it from Wikidata.",
    )
    args = parser.parse_args()

    print("Enriching persons from Wikidata...")
    print(f"input: {args.input}")
    print(f"persons cache: {args.persons_cache}")
    print(f"overwrite existing values: {args.overwrite}")
    print(f"refresh persons cache: {args.refresh_persons_cache}")

    print("Loading persons JSON...")
    payload = load_json(args.input)
    print("Loading persons cache...")
    persons_cache = load_wikidata_cache(args.persons_cache)

    print("Running Wikidata enrichment for persons...")
    enriched_payload, persons_cache, stats = enrich_person_links(
        payload,
        persons_cache,
        overwrite=args.overwrite,
        refresh_cache=args.refresh_persons_cache,
        pause_seconds=args.pause_seconds,
    )
    print("Writing enriched persons JSON...")
    save_json(args.input, enriched_payload)
    print("Writing persons cache...")
    save_json(args.persons_cache, persons_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {args.input}")
    print(f"persons cache: {args.persons_cache}")


if __name__ == "__main__":
    main()
