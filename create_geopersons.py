from pathlib import Path

from projectlibs.py.enrich_utils import load_json, save_json
from projectlibs.py.postprocessors.geopersons import create_person_life_trajectory
from projectlibs.py.postprocessors.utils import format_placeholders

PERSONS_FILE = Path("data/persons.json")
LOCATIONS_FILE = Path("data/locations.json")
LITERATURE_FILE = Path("data/literature.json")
MANUSCRIPTS_FILE = Path("data/manuscripts.json")
ARCHIVES_FILE = Path("data/archives.json")
COLLECTIONS_FILE = Path("data/collections.json")
OUTPUT_FILE = Path("data/geopersons.json")


def main() -> None:
    print()
    print("Running create_geopersons.py")
    persons = load_json(PERSONS_FILE)
    tables = {
        "locations": load_json(LOCATIONS_FILE),
        "literature": load_json(LITERATURE_FILE),
        "manuscripts": load_json(MANUSCRIPTS_FILE),
        "archives": load_json(ARCHIVES_FILE),
        "collections": load_json(COLLECTIONS_FILE),
    }

    transformed_persons = {}

    for person_id, person_record in persons.items():
        geoperson = create_person_life_trajectory(person_record, tables)
        geoperson = format_placeholders(geoperson, tables)
        transformed_persons[person_id] = geoperson

    save_json(OUTPUT_FILE, transformed_persons)
    print(f"Finished. output={OUTPUT_FILE}")


if __name__ == "__main__":
    main()
