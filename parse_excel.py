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


TEST_IDS = {
    "Personen": ["P0010000", "P0170000", "P0220000"],
}


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


def write_errors(file_path: str, errors: dict):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# Parsing Errors\n")
        for entity_id, field_errors in errors.items():
            for column, raw, message in field_errors:
                f.write(f"\n- [ ] __{entity_id}, {column}__:\n")
                f.write(f" _{message}_\n")
                f.write(f"> {raw}\n")


persons_df = load_excel_sheet(EXCEL_FILE, "Personen")

persons = {}
persons_errors = {}
for index, row in persons_df.iterrows():
    print(f"Personen: {row['ID']}")
    obj = HerrnhutPerson(row.to_dict())
    if obj._errors:
        persons_errors[row["ID"]] = obj._errors
    persons[obj.id] = obj
write_errors("validation_msgs/person_errors.md", persons_errors)

archives_df = load_excel_sheet(EXCEL_FILE, "Archive")

archives = {}
archives_errors = {}
for index, row in archives_df.iterrows():
    print(f"Archive: {row['ID']}")
    obj = HerrnhutArchive(row.to_dict())
    if obj._errors:
        archives_errors[row["ID"]] = obj._errors
    archives[obj.id] = obj
write_errors("validation_msgs/archive_errors.md", archives_errors)

manuscripts_df = load_excel_sheet(EXCEL_FILE, "Manuskripte")

manuscripts = {}
manuscripts_errors = {}
for index, row in manuscripts_df.iterrows():
    print(f"Manuskripte: {row['ID']}")
    obj = HerrnhutManuscript(row.to_dict())
    if obj._errors:
        manuscripts_errors[row["ID"]] = obj._errors
    manuscripts[obj.id] = obj
write_errors("validation_msgs/manuscript_errors.md", manuscripts_errors)

literature_df = load_excel_sheet(EXCEL_FILE, "Literatur")

literature = {}
literature_errors = {}
for index, row in literature_df.iterrows():
    print(f"Literatur: {row['ID']}")
    obj = HerrnhutLiterature(row.to_dict())
    if obj._errors:
        literature_errors[row["ID"]] = obj._errors
    literature[obj.id] = obj
write_errors("validation_msgs/literature_errors.md", literature_errors)

locations_df = load_excel_sheet(EXCEL_FILE, "Orte")

locations = {}
locations_errors = {}
for index, row in locations_df.iterrows():
    print(f"Orte: {row['ID']}")
    obj = HerrnhutLocation(row.to_dict())
    if obj._errors:
        locations_errors[row["ID"]] = obj._errors
    locations[obj.id] = obj
write_errors("validation_msgs/location_errors.md", locations_errors)

collections_df = load_excel_sheet(EXCEL_FILE, "Sammlungen")

collections = {}
collections_errors = {}
for index, row in collections_df.iterrows():
    print(f"Sammlungen: {row['ID']}")
    obj = HerrnhutCollection(row.to_dict())
    if obj._errors:
        collections_errors[row["ID"]] = obj._errors
    collections[obj.id] = obj
write_errors("validation_msgs/collection_errors.md", collections_errors)
