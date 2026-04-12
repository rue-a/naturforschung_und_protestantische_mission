def extract_field_value(field):
    return field["value"]["value"]


def format_reference(source_id, source_type, tables):
    if not source_id or not source_type:
        return source_id

    if source_type == "URL":
        return f"(Web) {source_id}"

    if source_type == "LiteratureID":
        literature = tables["literature"].get(source_id)

        parts = []
        if "title" in literature:
            parts.append(extract_field_value(literature["title"]))
        if "permalink" in literature:
            parts.append(extract_field_value(literature["permalink"]))
        if "description" in literature:
            parts.append(extract_field_value(literature["description"]))
        if not parts:
            parts.append(source_id)
        return f"(Druck) {' | '.join(parts)}"

    if source_type == "ManuscriptID":
        manuscript = tables["manuscripts"].get(source_id)

        parts = []

        if "archive" in manuscript:
            archive_id = extract_field_value(manuscript["archive"])
            archive = tables["archives"].get(archive_id)
            if archive and "name" in archive:
                parts.append(extract_field_value(archive["name"]))
            else:
                parts.append(archive_id)

        if "signature" in manuscript:
            parts.append(extract_field_value(manuscript["signature"]))
        if "title" in manuscript:
            parts.append(extract_field_value(manuscript["title"]))
        if "permalink" in manuscript:
            parts.append(extract_field_value(manuscript["permalink"]))
        if "description" in manuscript:
            parts.append(extract_field_value(manuscript["description"]))

        if not parts:
            parts.append(source_id)
        return f"(Manuscript) {' | '.join(parts)}"

    if source_type == "CollectionID":
        collection = tables["collections"].get(source_id)
        if not collection:
            return source_id

        herbarium_code = (
            extract_field_value(collection["nybg_herbarium_code"])
            if "nybg_herbarium_code" in collection
            else source_id
        )
        collection_name = (
            extract_field_value(collection["collection_name"])
            if "collection_name" in collection
            else ""
        )
        if "holding_institution" in collection:
            institutions = [
                entry["value"]
                for entry in collection["holding_institution"]["value"]["value"]
            ]
            institution = ", ".join(institutions) if institutions else ""
        else:
            institution = ""

        main_parts = [herbarium_code, collection_name]
        main_text = ", ".join(part for part in main_parts if part)

        if institution:
            return f"{main_text} ({institution})"

        return main_text

    return source_id


def replace_reference_objects(value, tables):
    if isinstance(value, list):
        return [replace_reference_objects(item, tables) for item in value]

    if isinstance(value, dict):
        value_type = value.get("type")

        if value_type in {"URL", "LiteratureID", "ManuscriptID", "CollectionID"}:
            return format_reference(value.get("value"), value_type, tables)

        return {
            key: replace_reference_objects(item, tables) for key, item in value.items()
        }

    return value
