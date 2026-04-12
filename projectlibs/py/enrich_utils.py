import json
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=4)
        handle.write("\n")


def typed_value(value: Any) -> dict[str, Any]:
    if isinstance(value, bool):
        return {"type": "Boolean", "value": value}
    if isinstance(value, str):
        return {"type": "String", "value": value}
    if isinstance(value, int):
        return {"type": "Integer", "value": value}
    if isinstance(value, float):
        return {"type": "Decimal", "value": value}
    if value is None:
        return {"type": "Null", "value": None}
    if isinstance(value, list):
        return {"type": "List", "value": [typed_value(item) for item in value]}
    if isinstance(value, dict):
        return {
            "type": "Object",
            "value": {key: typed_value(item) for key, item in value.items()},
        }
    return {"type": "String", "value": str(value)}


def make_url_field(label: str, value: str) -> dict[str, Any]:
    return {
        "label": label,
        "value": {
            "type": "URL",
            "value": value,
        },
    }


def make_decimal_field(label: str, value: float) -> dict[str, Any]:
    return {
        "label": label,
        "value": {
            "type": "Decimal",
            "value": value,
        },
    }


def make_string_field(label: str, value: str, *, type_name: str = "String") -> dict[str, Any]:
    return {
        "label": label,
        "value": {
            "type": type_name,
            "value": value,
        },
    }


def make_list_field(label: str, values: list[str], *, item_type: str = "String") -> dict[str, Any]:
    return {
        "label": label,
        "value": {
            "type": "List",
            "value": [{"type": item_type, "value": value} for value in values],
        },
    }


def make_object_field(label: str, value: dict[str, Any]) -> dict[str, Any]:
    return {
        "label": label,
        "value": typed_value(value),
    }


def extract_url_field(field: dict[str, Any] | None) -> str | None:
    if not isinstance(field, dict):
        return None
    value = field.get("value", {})
    if value.get("type") != "URL":
        return None
    return value.get("value")


def fetch_json(url: str, *, user_agent: str, accept: str = "application/json") -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": accept,
        },
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)
