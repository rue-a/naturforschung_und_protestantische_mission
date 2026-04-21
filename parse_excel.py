import pandas as pd
from projectlibs.py.herrnhut_objects import (
    HerrnhutPerson,
    HerrnhutArchive,
    HerrnhutManuscript,
    HerrnhutLiterature,
    HerrnhutLocation,
    HerrnhutCollection,
)

EXCEL_FILE = "data/Herrnhuter NaturkundlerInnen.xlsx"


PERSONS_TEST_IDS = ["P0010000", "P0170000", "P0220000"]


def load_excel_sheet(file_name, sheet_name):

    df = pd.read_excel(
        file_name,
        sheet_name=sheet_name,
        dtype=str,
        keep_default_na=False,
    )

    # col names in the excel are defined as <col-name><obligation-indicator>\n<datatype>
    # we remove the the obligation indicators and the line break and everything
    # that follows, so that only the actucal column name remains.
    df = df.rename(
        columns=lambda c: c.replace("*", "").replace("°", "").split("\n")[0].strip()
    )

    return df


# df = df.filter(items=list(sheet_specs.keys()))


ERRORS_FILE = "validation_msgs/errors.md"


def write_errors(file_path: str, all_errors: dict):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# Parsing Errors\n")
        for sheet_name, sheet_errors in all_errors.items():
            if not sheet_errors:
                continue
            f.write(f"\n## {sheet_name}\n")
            for entity_id, field_errors in sheet_errors.items():
                f.write(f"\n### {entity_id}\n")
                for column, causing, full_raw, message in field_errors:
                    while "\n\n" in full_raw:
                        full_raw = full_raw.replace("\n\n", "\n")
                    full_raw = full_raw.strip("\n")
                    causing = causing.strip("\n")
                    f.write(f"\n- [ ] **{column}** ({entity_id}):\n")
                    f.write(f"  - Error Message: **`{message}`**\n")
                    f.write(f"  - Causing raw value: `{causing}`\n")
                    if causing.strip() != full_raw.strip() and len(full_raw) < 400:
                        f.write(f"  - Full field: _{full_raw}_\n")


def load_objects(sheet_name: str, constructor, all_errors: dict, test_ids=None) -> dict:
    df = load_excel_sheet(EXCEL_FILE, sheet_name)
    objects = {}
    errors = {}
    for _, row in df.iterrows():
        if test_ids and row["ID"] not in test_ids:
            continue
        print(f"{sheet_name}: {row['ID']}")
        obj = constructor(row.to_dict())
        if obj._errors:
            errors[row["ID"]] = obj._errors
        objects[obj.id] = obj
    all_errors[sheet_name] = errors
    return objects


all_errors = {}
persons = load_objects(
    "Personen", HerrnhutPerson, all_errors, test_ids=PERSONS_TEST_IDS
)
archives = load_objects("Archive", HerrnhutArchive, all_errors)
manuscripts = load_objects("Manuskripte", HerrnhutManuscript, all_errors)
literature = load_objects("Literatur", HerrnhutLiterature, all_errors)
locations = load_objects("Orte", HerrnhutLocation, all_errors)
collections = load_objects("Sammlungen", HerrnhutCollection, all_errors)
write_errors(ERRORS_FILE, all_errors)
