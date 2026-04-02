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

    return source_id


def replace_reference_objects(value, tables):
    if isinstance(value, list):
        return [replace_reference_objects(item, tables) for item in value]

    if isinstance(value, dict):
        value_type = value.get("type")

        if value_type in {"URL", "LiteratureID", "ManuscriptID"}:
            return format_reference(value.get("value"), value_type, tables)

        return {
            key: replace_reference_objects(item, tables) for key, item in value.items()
        }

    return value
