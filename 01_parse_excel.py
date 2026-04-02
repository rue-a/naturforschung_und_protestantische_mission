import json

from projectlibs.py.table_parser import TableParser, DomainEncoder
from projectlibs.py.postprocessors.persons import transform_person_life_trajectory

from projectlibs.py.parsers import (
    PARSERS_PERSONEN,
    PARSERS_SAMMLUNGEN,
    PARSERS_ARCHIVE,
    PARSERS_LITERATUR,
    PARSERS_MANUSKRIPTE,
    PARSERS_ORTE,
)

EXCEL_FILE = "data/Herrnhuter NaturkundlerInnen.xlsx"


TABLES = {
    "Orte": {
        "spec": PARSERS_ORTE,
        "json": "data/locations.json",
        "errors": "todo/location_errors.md",
    },
    "Personen": {
        "spec": PARSERS_PERSONEN,
        "json": "data/persons.json",
        "errors": "todo/person_errors.md",
    },
    "Sammlungen": {
        "spec": PARSERS_SAMMLUNGEN,
        "json": "data/collections.json",
        "errors": "todo/collection_errors.md",
    },
    "Archive": {
        "spec": PARSERS_ARCHIVE,
        "json": "data/archives.json",
        "errors": "todo/archive_errors.md",
    },
    "Literatur": {
        "spec": PARSERS_LITERATUR,
        "json": "data/literature.json",
        "errors": "todo/literature_errors.md",
    },
    "Manuskripte": {
        "spec": PARSERS_MANUSKRIPTE,
        "json": "data/manuscripts.json",
        "errors": "todo/manuscript_errors.md",
    },
}


TEST_IDS = {
    "Personen": ["P0010000", "P0170000", "P0220000"],
}


def main():
    parsed_tables = {}

    for sheet, cfg in TABLES.items():
        print(f"Parsing {sheet}...")

        parser = TableParser(
            sheet_name=sheet,
            parser_specs=cfg["spec"],
            excel_file=EXCEL_FILE,
        )

        parsed = parser.run(
            output_json=cfg["json"],
            error_file=cfg["errors"],
            test_ids=TEST_IDS.get(sheet),
        )
        parsed_tables[sheet] = parsed

    print("Postprocessing Personen...")
    persons = parsed_tables["Personen"]
    locations = parsed_tables["Orte"]
    postprocessed_persons = {
        person_id: transform_person_life_trajectory(person_record, locations)
        for person_id, person_record in persons.items()
    }

    with open(TABLES["Personen"]["json"], "w", encoding="utf-8") as f:
        json.dump(
            postprocessed_persons,
            f,
            ensure_ascii=False,
            indent=4,
            cls=DomainEncoder,
        )


if __name__ == "__main__":
    main()
