def extract_field_value(field):
    if not field:
        return None
    try:
        return field["value"]["value"]
    except (TypeError, KeyError):
        print(f"Warning: could not extract field value from {field!r}")
        return None


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


def format_moravian_membership_field(field):
    formatted_field = dict(field)
    formatted_value = dict(field["value"])
    formatted_entries = []

    for entry in field["value"]["value"]:
        if isinstance(entry, dict):
            formatted_entry = dict(entry)
            code = entry.get("value")
            formatted_entry["value"] = MORAVIAN_MEMBERSHIP_LABELS.get(code, code)
            formatted_entries.append(formatted_entry)
        else:
            formatted_entries.append(MORAVIAN_MEMBERSHIP_LABELS.get(entry, entry))

    formatted_value["value"] = formatted_entries
    formatted_field["value"] = formatted_value
    return formatted_field


def format_collection_id(collection_id, collections):
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


def format_web_reference(url):
    if not url:
        return url

    return f"(Web) {url}"


def format_literature_reference(literature_id, literature_table):
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


def format_manuscript_reference(manuscript_id, manuscripts, archives):
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


def format_location_id(location_id, locations):
    location = locations.get(location_id)
    if not location:
        print(f"Warning: could not resolve LocationID {location_id}")
        return location_id

    location_name = extract_field_value(location.get("name")) or location_id
    wikidata_link = extract_field_value(location.get("wikidata_link"))
    if not wikidata_link:
        return location_name

    return f'<a href="{wikidata_link}">{location_name}</a>'


def format_placeholders(value, tables):
    locations = tables["locations"]
    collections = tables["collections"]
    literature_table = tables["literature"]
    manuscripts = tables["manuscripts"]
    archives = tables["archives"]

    if isinstance(value, list):
        return [format_placeholders(item, tables) for item in value]

    if isinstance(value, dict):
        if (
            value.get("excel-column-name")
            == "Zugehörigkeit Herrnhuter Brüdergemeine"
            and value.get("value", {}).get("type") == "List"
        ):
            return format_moravian_membership_field(value)

        if (
            "value" in value
            and isinstance(value["value"], dict)
            and value["value"].get("type") == "LocationID"
        ):
            location_value = value["value"]
            formatted_location = format_location_id(location_value["value"], locations)
            resolved_field = dict(value)
            resolved_field["value"] = {
                "type": "String",
                "value": formatted_location,
            }
            if "source" in location_value:
                resolved_field["value"]["source"] = location_value["source"]
            return resolved_field

        value_type = value.get("type")

        if value_type == "CollectionID":
            return format_collection_id(value.get("value"), collections)

        if value_type == "URL":
            return format_web_reference(value.get("value"))

        if value_type == "LiteratureID":
            return format_literature_reference(value.get("value"), literature_table)

        if value_type == "ManuscriptID":
            return format_manuscript_reference(value.get("value"), manuscripts, archives)

        return {key: format_placeholders(item, tables) for key, item in value.items()}

    return value
