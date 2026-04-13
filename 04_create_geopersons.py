from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.postprocessors.persons import transform_person_life_trajectory

PERSONS_FILE = Path("data/persons.json")
LOCATIONS_FILE = Path("data/locations.json")
LITERATURE_FILE = Path("data/literature.json")
MANUSCRIPTS_FILE = Path("data/manuscripts.json")
ARCHIVES_FILE = Path("data/archives.json")
COLLECTIONS_FILE = Path("data/collections.json")
OUTPUT_FILE = Path("data/geopersons.json")


def main(
    persons_file: Path = PERSONS_FILE,
    locations_file: Path = LOCATIONS_FILE,
    literature_file: Path = LITERATURE_FILE,
    manuscripts_file: Path = MANUSCRIPTS_FILE,
    archives_file: Path = ARCHIVES_FILE,
    collections_file: Path = COLLECTIONS_FILE,
    output_file: Path = OUTPUT_FILE,
) -> None:
    persons = load_json(persons_file)
    tables = {
        "locations": load_json(locations_file),
        "literature": load_json(literature_file),
        "manuscripts": load_json(manuscripts_file),
        "archives": load_json(archives_file),
        "collections": load_json(collections_file),
    }

    transformed_persons = {
        person_id: transform_person_life_trajectory(person_record, tables)
        for person_id, person_record in persons.items()
    }

    save_json(output_file, transformed_persons)
    print(f"Finished. output={output_file}")


if __name__ == "__main__":
    main()
