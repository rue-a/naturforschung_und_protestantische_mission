from projectlibs.py.table_parser import TableParser

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
    for sheet, cfg in TABLES.items():
        print(f"Parsing {sheet}...")

        parser = TableParser(
            sheet_name=sheet,
            parser_specs=cfg["spec"],
            excel_file=EXCEL_FILE,
        )

        parser.run(
            output_json=cfg["json"],
            error_file=cfg["errors"],
            test_ids=TEST_IDS.get(sheet),
        )


if __name__ == "__main__":
    main()
