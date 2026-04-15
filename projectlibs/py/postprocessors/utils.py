def extract_field_value(field):
    if not field:
        return None
    try:
        return field["value"]["value"]
    except (TypeError, KeyError):
        print(f"Warning: could not extract field value from {field!r}")
        return None


def replace_typed_values(node, replacements):
    """
    Recursively walk a nested typed-value structure and replace values based on
    their declared type.

    `replacements` maps a type name to a callable. Each callable receives the
    already-recursively-processed value and the full typed node, and must return
    the replacement value for that node.

    Example:
        replacements = {
            "LocationID": lambda value, _: location_labels.get(value, value),
            "LiteratureID": lambda value, _: {"id": value, "kind": "literature"},
        }
    """
    if isinstance(node, list):
        return [replace_typed_values(item, replacements) for item in node]

    if not isinstance(node, dict):
        return node

    transformed = {
        key: replace_typed_values(value, replacements) for key, value in node.items()
    }

    node_type = transformed.get("type")
    if isinstance(node_type, str) and "value" in transformed and node_type in replacements:
        transformed["value"] = replacements[node_type](
            transformed["value"],
            transformed,
        )

    return transformed
