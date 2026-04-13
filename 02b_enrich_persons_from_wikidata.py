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


def main(
    input_path: Path = DEFAULT_INPUT,
    overwrite: bool = OVERWRITE,
    pause_seconds: float = PAUSE_SECONDS,
    persons_cache_path: Path = PERSONS_CACHE,
    refresh_persons_cache: bool = REFRESH_PERSONS_CACHE,
) -> None:
    print("Enriching persons from Wikidata...")
    print(f"input: {input_path}")
    print(f"persons cache: {persons_cache_path}")
    print(f"overwrite existing values: {overwrite}")
    print(f"refresh persons cache: {refresh_persons_cache}")

    print("Loading persons JSON...")
    payload = load_json(input_path)
    print("Loading persons cache...")
    persons_cache = load_wikidata_cache(persons_cache_path)

    print("Running Wikidata enrichment for persons...")
    enriched_payload, persons_cache, stats = enrich_person_links(
        payload,
        persons_cache,
        overwrite=overwrite,
        refresh_cache=refresh_persons_cache,
        pause_seconds=pause_seconds,
    )
    print("Writing enriched persons JSON...")
    save_json(input_path, enriched_payload)
    print("Writing persons cache...")
    save_json(persons_cache_path, persons_cache)

    print("Finished.")
    print(
        f"updated={stats['updated']} skipped={stats['skipped']} failed={stats['failed']}"
    )
    print(f"output: {input_path}")
    print(f"persons cache: {persons_cache_path}")


if __name__ == "__main__":
    main()
