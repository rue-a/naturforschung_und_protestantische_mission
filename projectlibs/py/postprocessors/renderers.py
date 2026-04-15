from pathlib import Path

from projectlibs.py.postprocessors.utils import extract_field_value
from projectlibs.py.enrich_utils import load_json

PERSONS = load_json(Path("data/persons.json"))
LOCATIONS = load_json(Path("data/locations.json"))
LITERATURE = load_json(Path("data/literature.json"))
MANUSCRIPTS = load_json(Path("data/manuscripts.json"))
ARCHIVES = load_json(Path("data/archives.json"))
COLLECTIONS = load_json(Path("data/collections.json"))


MORAVIAN_MEMBERSHIP_LABELS = {
    "ja(a)": "qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen",
    "ja(b)": "als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte",
    "ja(c)": "Übernahme von kirchlichen Ämtern innerhalb der Brüdergemeine",
    "ja(d)": "Übernahme von Ämtern im Erziehungswesen der Brüdergemeine",
    "nein(a)": "ausgetreten",
    "nein(b)": "aber wichtig im Netzwerk",
    "nein(c)": "um Verwechslung auszuschließen",
    "unbekannt": "Zugehörigkeit kann nicht ausgeschlossen werden.",
}


def render_collection_id(collection_id, collections):
    collection = collections.get(collection_id)
    if not collection:
        print(f"Warning: could not resolve CollectionID {collection_id}")
        return collection_id

    herbarium_code = (
        extract_field_value(collection.get("nybg_herbarium_code")) or collection_id
    )
    collection_name = extract_field_value(collection.get("collection_name")) or ""
    institution_values = (
        extract_field_value(collection.get("holding_institution")) or []
    )
    institution = ", ".join(
        entry["value"]
        for entry in institution_values
        if isinstance(entry, dict) and "value" in entry
    )
    collection_text = ", ".join(
        part for part in [herbarium_code, collection_name] if part
    )

    if institution:
        return f"{collection_text} ({institution})"

    return collection_text or collection_id


def render_web_reference(url):
    return f"(Web) {url}"


def render_literature_id(literature_id, literature_table):
    literature = literature_table.get(literature_id)
    if not literature:
        print(f"Warning: could not resolve LiteratureID {literature_id}")
        return literature_id

    parts = []
    parts.append(extract_field_value(literature.get("title")))
    parts.append(extract_field_value(literature.get("permalink")))
    parts.append(extract_field_value(literature.get("description")))
    parts = [part for part in parts if part]
    if not parts:
        parts.append(literature_id)
    return f"(Druck) {' | '.join(parts)}"


def render_manuscript_id(manuscript_id, manuscripts, archives):
    manuscript = manuscripts.get(manuscript_id)
    if not manuscript:
        print(f"Warning: could not resolve ManuscriptID {manuscript_id}")
        return manuscript_id

    parts = []

    archive_id = extract_field_value(manuscript.get("archive"))
    if archive_id:
        archive = archives.get(archive_id)
        archive_name = extract_field_value(archive.get("name")) if archive else None
        parts.append(archive_name or archive_id)

    parts.append(extract_field_value(manuscript.get("signature")))
    parts.append(extract_field_value(manuscript.get("title")))
    parts.append(extract_field_value(manuscript.get("permalink")))
    parts.append(extract_field_value(manuscript.get("description")))
    parts = [part for part in parts if part]

    if not parts:
        parts.append(manuscript_id)
    return f"(Manuscript) {' | '.join(parts)}"


def render_location_id(location_id, locations):
    location = locations.get(location_id)
    if not location:
        print(f"Warning: could not resolve LocationID {location_id}")
        return location_id

    location_name = extract_field_value(location.get("name")) or location_id
    wikidata_link = extract_field_value(location.get("wikidata_link"))
    if not wikidata_link:
        return location_name

    return f'<a href="{wikidata_link}">{location_name}</a>'


def render_person_id(person_id, persons):
    person = persons.get(person_id)
    if not person:
        print(f"Warning: could not resolve PersonID {person_id}")
        return person_id

    preferred_name = extract_field_value(person.get("name", {}).get("preferred"))
    return preferred_name or person_id


def render_codelist_value(value, codelist):
    return codelist[value]


# You need lambda when the function requires extra arguments that are not part of the "value".
TYPE_RENDERERS = {
    "LocationID": lambda value: render_location_id(value, LOCATIONS),
    "CollectionID": lambda value: render_collection_id(value, COLLECTIONS),
    "PersonID": lambda value: render_person_id(value, PERSONS),
    "URL": render_web_reference,
    "LiteratureID": lambda value: render_literature_id(value, LITERATURE),
    "ManuscriptID": lambda value: render_manuscript_id(value, MANUSCRIPTS, ARCHIVES),
    "MoravianMembership": lambda value: render_codelist_value(
        value, MORAVIAN_MEMBERSHIP_LABELS
    ),
    "ISO8601_2_Temporal": lambda value: value,
    "ISO8601_2_Date": lambda value: value,
    "ISO8601_2_Interval": lambda value: value,
    "String": lambda value: value,  # return value
    "Null": lambda value: "",
    # "ComplexType": lambda value: value,
    # "List": lambda value: value,
}


def replace_typed_nodes(data, renderers=TYPE_RENDERERS):
    """
    Recursively replace dicts of shape {"type": ..., "value": ...}
    with their rendered value if type is supported.
    """
    if isinstance(data, list):
        print(data)
        return [replace_typed_nodes(item) for item in data]

    if isinstance(data, dict):
        # If this is a typed node → replace entire dict
        if "type" in data and "value" in data:
            field_type = data["type"]
            value = data["value"]
            # if field_type == "List":
            #     return replace_typed_nodes(value)

            if field_type in renderers:
                return renderers[field_type](value)

        # Otherwise recurse into dict
        return {key: replace_typed_nodes(value) for key, value in data.items()}

    return data
