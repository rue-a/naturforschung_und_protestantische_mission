import re
from dataclasses import dataclass
from datetime import date
from abc import ABC, abstractmethod
from typing import Optional, Union


# -----------------------
# Base class for attestable datatypes
# -----------------------
from abc import ABC, abstractmethod


class Attestable(ABC):
    STRUCTURED_PATTERN = re.compile(r"^(.*?)\s*\((.*?)\)$")  # value + reference

    @abstractmethod
    def _validate_value(self, value: str):
        """Validate the raw value. Must be implemented by subclasses."""
        pass

    def __init__(self, raw: str):
        raw = raw.strip()
        if not raw:
            raise ValueError("Cannot parse empty string")

        m = self.STRUCTURED_PATTERN.fullmatch(raw)
        if m:
            value_str, ref_str = m.groups()
            object.__setattr__(self, "source", Reference(ref_str) if ref_str else None)
        else:
            value_str = raw
            object.__setattr__(self, "source", None)

        self._validate_value(value_str)
        object.__setattr__(self, "value", value_str)


# -----------------------
# Reference type
# -----------------------
@dataclass(frozen=True)
class Reference:
    value: str

    def __post_init__(self):
        # Reference can be a URL or an ID
        for parser in (URL, ID):
            try:
                parser(self.value)
                return
            except ValueError:
                pass
        raise ValueError(
            f"Invalid Reference value: {self.value!r} (should be URL, R-ID, or M-ID)"
        )


# -----------------------
# URL type
# -----------------------
@dataclass(frozen=True)
class URL:
    value: str

    def __post_init__(self):
        if not re.fullmatch(r"^https?://", self.value):
            raise ValueError(
                f"URL must start with 'http://' or 'https://': {self.value!r}"
            )


# -----------------------
# ID type (attestable)
# -----------------------
class ID(Attestable):
    """An alphanumeric, unique identifier for objects within this project"""

    def _validate_value(self, value: str):
        # Pattern: persons P + 7 digits, literature R + 7 digits, collections C-...
        pattern = r"(?:^[PRLMA]\d{7}$)|(?:^C-.+$)"
        if not re.fullmatch(pattern, value):
            raise ValueError(f"Invalid ID format: {value!r}")


# -----------------------
# ISO Date type (attestable)
# -----------------------
class ISO_Date(Attestable):
    """Exact date in YYYY-MM-DD format"""

    def _validate_value(self, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Invalid ISO date string: {value!r}")


# -----------------------
# ISO8601-2 Date type (attestable)
# -----------------------
class ISO8601_2_Date(Attestable):
    """Day- to year-level ISO8601-2 date"""

    def _validate_value(self, value: str):
        pattern = r"^(\d{4})(-\d{2})?(-\d{2})?([~%?])?$"
        if not re.fullmatch(pattern, value):
            raise ValueError(f"Invalid ISO8601-2_Date format: {value!r}")


# -----------------------
# ISO8601-2 Period type (attestable)
# -----------------------
class ISO8601_2_Period(Attestable):
    """Time period using two ISO8601-2_Date strings"""

    def _validate_value(self, value: str):
        parts = value.split("/")
        if len(parts) != 2:
            raise ValueError(
                f"Invalid period format: {value!r}, must have exactly one '/'"
            )
        start, end = parts
        if start:
            ISO8601_2_Date(start)
        if end:
            ISO8601_2_Date(end)


# -----------------------
# ISO8601-2 Temporal type (attestable)
# -----------------------
class ISO8601_2_Temporal(Attestable):
    """Contains ISO8601-2_Date or ISO8601-2_Period"""

    def _validate_value(self, value: str):
        for parser in (ISO8601_2_Date, ISO8601_2_Period):
            try:
                parser(value)
                return
            except ValueError:
                pass
        raise ValueError(f"Invalid Temporal value: {value!r}")
