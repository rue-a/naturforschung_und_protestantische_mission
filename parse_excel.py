# %%
import json
import pandas as pd
from projectlibs.py.herrnhut_objects import (
    HerrnhutPerson,
    HerrnhutArchive,
    HerrnhutManuscript,
    HerrnhutLiterature,
    HerrnhutLocation,
    HerrnhutCollection,
)
from projectlibs.py.helpers.registry import Registry

EXCEL_FILE = "data/Herrnhuter NaturkundlerInnen.xlsx"

# PERSONS_TEST_IDS = ["P0010000", "P0170000", "P0220000"]
PERSONS_TEST_IDS = None

ERRORS_FILE = "validation_msgs/errors.md"

PERSONS_CACHE = "data/cache_persons_wikidata.json"
LOCATIONS_CACHE = "data/cache_locations_wikidata.json"
REWRITE_CACHE = False

PERSONS_OUTPUT = "data/persons.json"
LOCATIONS_OUTPUT = "data/locations.json"


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
        if not row["ID"].strip():
            continue
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

print("--- Loading objects from Excel ---")
persons = load_objects(
    "Personen", HerrnhutPerson, all_errors, test_ids=PERSONS_TEST_IDS
)
archives = load_objects("Archive", HerrnhutArchive, all_errors)
manuscripts = load_objects("Manuskripte", HerrnhutManuscript, all_errors)
literature = load_objects("Literatur", HerrnhutLiterature, all_errors)
locations = load_objects("Orte", HerrnhutLocation, all_errors)
collections = load_objects("Sammlungen", HerrnhutCollection, all_errors)

write_errors(ERRORS_FILE, all_errors)
print(f"Parsing errors written to {ERRORS_FILE}")

print("--- Enriching ---")
for obj_id, location in locations.items():
    print(f"Enriching location {obj_id}")
    location.enrich(LOCATIONS_CACHE, rewrite_cache=REWRITE_CACHE)

for obj_id, person in persons.items():
    print(f"Enriching person {obj_id}")
    person.enrich(PERSONS_CACHE, rewrite_cache=REWRITE_CACHE)

print("--- Building life trajectories ---")
for obj_id, person in persons.items():
    print(f"Building life trajectory for {obj_id}")
    person._create_life_trajectory(locations)

print("Done.")

print("--- Serializing ---")
registry = Registry(
    persons=persons,
    locations=locations,
    archives=archives,
    manuscripts=manuscripts,
    literature=literature,
    collections=collections,
)

persons_out = [p.to_dict(registry) for p in persons.values()]

importance = HerrnhutLocation.compute_importance(persons)
_zero = {"births": [], "deaths": [], "places_of_effect": []}

location_features = [loc.to_dict(registry) for loc in locations.values()]
for feature in location_features:
    feature["properties"]["importance"] = importance.get(feature["id"], _zero)

locations_out = {
    "type": "FeatureCollection",
    "conformsTo": ["http://www.opengis.net/spec/json-fg-1/0.2/conf/core"],
    "features": location_features,
}

with open(PERSONS_OUTPUT, "w", encoding="utf-8") as f:
    json.dump(persons_out, f, ensure_ascii=False, indent=2)
print(f"Written {PERSONS_OUTPUT}")

with open(LOCATIONS_OUTPUT, "w", encoding="utf-8") as f:
    json.dump(locations_out, f, ensure_ascii=False, indent=2)
print(f"Written {LOCATIONS_OUTPUT}")

# %%
# print(list(persons.values())[0].life_trajectory.to_dict())
