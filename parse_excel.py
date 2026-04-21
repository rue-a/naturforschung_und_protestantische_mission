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


persons_df = load_excel_sheet(EXCEL_FILE, "Personen")

persons = {}
for index, row in persons_df.iterrows():
    print(f"Personen: {row['ID']}")
    current_person = HerrnhutPerson(row.to_dict())
    persons[current_person.id] = current_person

archives_df = load_excel_sheet(EXCEL_FILE, "Archive")

archives = {}
for index, row in archives_df.iterrows():
    print(f"Archive: {row['ID']}")
    current_archive = HerrnhutArchive(row.to_dict())
    archives[current_archive.id] = current_archive

manuscripts_df = load_excel_sheet(EXCEL_FILE, "Manuskripte")

manuscripts = {}
for index, row in manuscripts_df.iterrows():
    print(f"Manuskripte: {row['ID']}")
    current_manuscript = HerrnhutManuscript(row.to_dict())
    manuscripts[current_manuscript.id] = current_manuscript

literature_df = load_excel_sheet(EXCEL_FILE, "Literatur")

literature = {}
for index, row in literature_df.iterrows():
    print(f"Literatur: {row['ID']}")
    current_literature = HerrnhutLiterature(row.to_dict())
    literature[current_literature.id] = current_literature

locations_df = load_excel_sheet(EXCEL_FILE, "Orte")

locations = {}
for index, row in locations_df.iterrows():
    print(f"Orte: {row['ID']}")
    current_location = HerrnhutLocation(row.to_dict())
    locations[current_location.id] = current_location

collections_df = load_excel_sheet(EXCEL_FILE, "Sammlungen")

collections = {}
for index, row in collections_df.iterrows():
    print(f"Sammlungen: {row['ID']}")
    current_collection = HerrnhutCollection(row.to_dict())
    collections[current_collection.id] = current_collection
