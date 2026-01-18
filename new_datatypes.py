import re
from dataclasses import dataclass
from datetime import date
from abc import ABC, abstractmethod


class Attestable(ABC):
    STRUCTURED_PATTERN = re.compile(r"^(.*?)\s*\((.*?)\)$")

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
            self.source = Reference(ref_str) if ref_str else None
        else:
            value_str = raw
            self.source = None

        self._validate_value(value_str)
        self.value = value_str


# -----------------------
# Reference type
# -----------------------
@dataclass(frozen=True)
class Reference:
    value: str

    def __post_init__(self):
        # Try URL first
        try:
            URL(self.value)
            return
        except ValueError:
            pass

        # Try ID validation
        try:
            ID(self.value)
            # Additional validation: IDs must start with M- or R-
            if not (self.value.startswith("M") or self.value.startswith("R")):
                raise ValueError(
                    f"Invalid ID format: {self.value!r} (must start with M or R)"
                )
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


# ID type (attestable)
# -----------------------
class ID(Attestable):
    """An alphanumeric, unique identifier for objects within this project"""

    def _validate_value(self, value: str):
        # Pattern: persons P + 7 digits, literature R + 7 digits, collections C-...
        pattern = r"(?:^[PRLMA]\d{7}$)|(?:^C-.+$)"
        if not re.fullmatch(pattern, value):
            raise ValueError(f"Invalid ID format: {value!r}")

    def __init__(self, raw: str):
        # Initialize the parent class first
        super().__init__(raw)
        # Now we can safely access self.value and set the type
        if self.value.startswith("P"):
            self.type = "person"
        elif self.value.startswith("R"):
            self.type = "literature"
        elif self.value.startswith("L"):
            self.type = "location"
        elif self.value.startswith("M"):
            self.type = "manuscript"
        elif self.value.startswith("A"):
            self.type = "archive"
        elif self.value.startswith("C"):
            self.type = "collection"
        else:
            raise ValueError(f"Unknown ID type for: {self.value!r}")


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
        # Check if it's a valid date first
        try:
            ISO8601_2_Date(value)
            self.type = "date"
            return
        except ValueError:
            pass

        # Check if it's a valid period
        try:
            ISO8601_2_Period(value)
            self.type = "period"
            return
        except ValueError:
            pass

        raise ValueError(f"Invalid Temporal value: {value!r}")


class ComplexType:
    """
    Parser for ordered, structured string values composed of multiple
    sub-values with an optional trailing reference.

    A ComplexType represents a *single structured value* inside a table cell.
    Multiple such values may be combined at field level using "|" and are
    handled by `parse_field`, not by this class.

    Structure rules
    ----------------
    - Sub-values are separated by a fixed separator (default: ";").
    - The number and order of sub-values is fixed.
    - Missing sub-values MUST still be represented by empty positions
      (i.e. consecutive separators), unless `allow_missing=False`.
    - A reference, if enabled, must appear exactly once at the very end
      of the value, enclosed in parentheses: "(...)".

    Example (Wirkungsort):
        1773/1782; L0000123; Knabenanstalt; Schüler (R0000456)

    Parsing behavior
    ----------------
    - The reference is parsed and validated using `Reference`.
    - Each sub-value is parsed using its corresponding parser callable
      (e.g. ID, ISO8601_2_Temporal, str).
    - Sub-values MUST NOT themselves contain references.
    - Optional validators may enforce semantic constraints on individual
      sub-values (e.g. requiring an L-ID for locations).

    Return value
    ------------
    A dictionary with two keys:
        - "values": tuple of parsed sub-values (or None for missing values)
        - "source": Reference instance or None

    This class is callable and is intended to be used directly as the
    `parser` argument in `ParserSpec`.

    Example usage:
        ParserSpec(
            parser=ComplexType(
                parts=[ISO8601_2_Temporal, ID, str, str],
                validators={1: require_L_ID},
            ),
            is_list=True,
        )
    """

    def __init__(
        self,
        *,
        parts: list[callable],
        separator: str = ";",
        reference: bool = True,
        allow_missing: bool = True,
        validators: dict[int, callable] | None = None,
    ):
        """
        parts: ordered list of parsers
        validators: optional index -> validator(value)
        """
        self.parts = parts
        self.separator = separator
        self.reference = reference
        self.allow_missing = allow_missing
        self.validators = validators or {}

    def __call__(self, raw: str):
        raw = raw.strip()
        if not raw:
            raise ValueError("Cannot parse empty complex value")

        # --- extract reference (only once, at the end) ---
        source = None
        if self.reference:
            m = Attestable.STRUCTURED_PATTERN.fullmatch(raw)
            if not m:
                raise ValueError("Missing reference for complex value")
            raw, ref_raw = m.groups()
            source = Reference(ref_raw)

        chunks = [c.strip() for c in raw.split(self.separator)]

        if len(chunks) != len(self.parts):
            raise ValueError(f"Expected {len(self.parts)} parts, got {len(chunks)}")

        values = []
        for idx, (parser, chunk) in enumerate(zip(self.parts, chunks)):
            if not chunk:
                if self.allow_missing:
                    values.append(None)
                    continue
                raise ValueError(f"Missing required part at position {idx}")

            # disallow nested references
            if "(" in chunk or ")" in chunk:
                raise ValueError(f"Reference not allowed inside part {idx}: {chunk!r}")

            value = parser(chunk)

            if idx in self.validators:
                # apply <value> (the validation function) to <idx> (the class attribute at the idx position)
                self.validators[idx](value)

            values.append(value)

        return {
            "values": tuple(values),
            "source": source,
        }
