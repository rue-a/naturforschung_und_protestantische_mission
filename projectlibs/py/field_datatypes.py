import re
from abc import ABC, abstractmethod
from validators import url

_DE_MONTHS = [
    "",
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember",
]


def _fmt_date(val: str) -> str:
    """Format an ISO 8601-2 date string into German notation."""
    parts = str(val).split("-")
    try:
        if len(parts) == 3:
            m = int(parts[1])
            if 1 <= m <= 12:
                return f"{int(parts[2])}. {_DE_MONTHS[m]} {parts[0]}"
        elif len(parts) == 2:
            m = int(parts[1])
            if 1 <= m <= 12:
                return f"{_DE_MONTHS[m]} {parts[0]}"
    except (ValueError, IndexError):
        pass
    return val


def clean_field(raw: str) -> str:
    """Normalize field before parsing
    IMPORTANT: Removes square brackets and anything inside!!
    """
    if not raw:
        return ""

    # remove all newlines
    raw = raw.replace("\n", "")

    # remove square brackets and their content
    raw = re.sub(r"\[.*?\]", "", raw)

    # collapse multiple spaces elsewhere
    raw = re.sub(r"\s+", " ", raw)

    # strip leading/trailing spaces
    raw = raw.strip()

    return raw


class AttestableDatatype(ABC):
    @abstractmethod
    def _parse_value(self, value: str):
        """Validate the raw value. Must be implemented by subclasses."""
        pass

    def _split_value_and_source(self, in_string: str, require_source):
        # get string in parantheses, if preceded by an empty space
        source_pattern = re.compile(r"^(.*?) \((.*?)\)$")

        match = source_pattern.fullmatch(in_string)
        if match:
            value, source = match.groups()
            if require_source and not source:
                raise ValueError(
                    f"Statement ({in_string}) requires attestation (no source was provided)!"
                )
            return value, source

        return in_string, None

    def __init__(self, raw: str, require_source=False, mandatory=False):

        raw = clean_field(raw)
        if not raw and not mandatory:
            return None
        self.raw = raw
        value, source_string = self._split_value_and_source(raw, require_source)
        if source_string:
            self.source = ReferenceDocument(source_string, require_source=False)
        else:
            self.source = None
        self._parse_value(value)

    def source_dict(self, registry=None) -> dict | None:
        """Serialize .source → {type, ...} dict or None. Registry is duck-typed."""
        if not hasattr(self, "source") or self.source is None:
            return None
        doc = getattr(self.source, "document", None)
        if doc is None:
            return None
        if hasattr(doc, "url"):
            return {"type": "web", "label": doc.url}
        if isinstance(doc, LiteratureID):
            ref = registry.resolve_literature(doc) if registry else {"id": doc.id}
            return {"type": "print", **{k: v for k, v in ref.items() if k != "source"}}
        ref = registry.resolve_manuscript(doc) if registry else {"id": doc.id}
        return {"type": "manuscript", **{k: v for k, v in ref.items() if k != "source"}}

    # -------------------------
    # PRINT SERIALIZATION
    # -------------------------

    def __str__(self) -> str:
        return self.raw


class ReferenceDocument(AttestableDatatype):
    """Source is either a URL, a LiteratureID or a ManuscriptID"""

    def _parse_value(self, document_string):
        # Try URL first
        try:
            self.document = URL(document_string)
            return
        except ValueError:
            pass

        # Try ID validation
        try:
            self.document = LiteratureID(document_string)
            return
        except ValueError:
            pass

        try:
            self.document = ManuscriptID(document_string)
            return
        except ValueError:
            pass

        raise ValueError(
            f"Invalid Reference Document value: {document_string} (should be URL, R-ID, or M-ID)"
        )


class WorkID(AttestableDatatype):
    """A work is either a LiteratureID or a ManuscriptID"""

    def _parse_value(self, work_id):

        try:
            self.document = LiteratureID(work_id)
            return
        except ValueError:
            pass

        try:
            self.document = ManuscriptID(work_id)
            return
        except ValueError:
            pass

        raise ValueError(f"Invalid work id: {work_id} (should be R-ID, or M-ID)")


class URL(AttestableDatatype):
    def _parse_value(self, url_string):
        # if not re.match(r"^https?://", url_string):
        #     raise ValueError(
        #         f"URL must start with 'http://' or 'https://': {url_string}"
        #     )
        if not url(url_string):
            raise ValueError(f"URL is not valid: {url_string}")
        self.url = url_string

    def to_dict(self, registry=None) -> dict:
        return {
            "label": getattr(self, "url", None),
            "source": self.source_dict(registry),
        }


class ID(AttestableDatatype, ABC):
    PREFIX: str = None
    PATTERN: str = None

    def _parse_value(self, value: str):
        if self.PREFIX is None:
            raise NotImplementedError("ID-classes must define PREFIX")

        if not value.startswith(self.PREFIX):
            raise ValueError(
                f"{self.__class__.__name__} must start with '{self.PREFIX}': {value}"
            )

        if self.PATTERN and not re.fullmatch(self.PATTERN, value):
            raise ValueError(f"Invalid format for {self.__class__.__name__}: {value}")

        self.id = value


class PersonID(ID):
    PREFIX = "P"
    PATTERN = r"^P\d{7}$"


class LiteratureID(ID):
    PREFIX = "R"
    PATTERN = r"^R\d{7}$"


class LocationID(ID):
    PREFIX = "L"
    PATTERN = r"^L\d{7}$"


class ManuscriptID(ID):
    PREFIX = "M"
    PATTERN = r"^M\d{7}$"


class ArchiveID(ID):
    PREFIX = "A"
    PATTERN = r"^A\d{7}$"


class CollectionID(ID):
    PREFIX = "C"
    PATTERN = r"^C-.+$"


class String(AttestableDatatype):
    """A string that can optionally carry a source (attestation)."""

    def _parse_value(self, value: str):
        # For a generic string, we accept anything
        self.value = value

    def to_dict(self, registry=None) -> dict:
        return {
            "label": getattr(self, "value", None),
            "source": self.source_dict(registry),
        }


class EncodedString(AttestableDatatype):
    """A string that has to adhere to codes from a codelist.
    The codelist is provided as a dict mapping codes to their decoded meaning.
    It is used for validation only and not stored on the instance."""

    def __init__(self, raw: str, codelist: dict, require_source=False):
        self._codelist = codelist
        super().__init__(raw, require_source=require_source)
        del self._codelist

    def _parse_value(self, value: str):
        if value not in self._codelist:
            raise ValueError(f"Provided string is not in codelist: {value}")
        self.encoded_value = value
        self.decoded_value = self._codelist[value]


class ISO8601_2_Temporal(AttestableDatatype):
    """Abstract base for ISO 8601-2 temporal values (date or period)."""

    @abstractmethod
    def formatted(self) -> str | None:
        """Return a human-readable German representation."""

    @abstractmethod
    def iso_string(self) -> str | None:
        """Return a machine readable ISO8601 string"""


class ISO8601_2_Date(ISO8601_2_Temporal):
    """Day- to year-level ISO8601-2 date"""

    def _parse_value(self, value: str):
        pattern = r"^(\d{4})(-\d{2})?(-\d{2})?([~%?])?$"
        if not re.fullmatch(pattern, value):
            raise ValueError(f"Invalid ISO8601-2_Date format: {value}")
        self.date = value

    def formatted(self) -> str | None:
        d = getattr(self, "date", None)
        return _fmt_date(d) if d else None

    def iso_string(self) -> str | None:
        return getattr(self, "date", None)

    def to_dict(self, registry=None) -> dict:
        return {"label": self.formatted(), "source": self.source_dict(registry)}


class ISO8601_2_Period(ISO8601_2_Temporal):
    """Time period using two ISO8601-2_Date strings"""

    def _parse_value(self, value: str):
        parts = value.split("/")
        if len(parts) != 2:
            raise ValueError(
                f"Invalid period format: {value}, must have exactly one '/'"
            )
        start, end = parts
        if start:
            self.start = ISO8601_2_Date(start)
        if end:
            self.end = ISO8601_2_Date(end)

    def formatted(self) -> str | None:
        start = getattr(getattr(self, "start", None), "date", None)
        end = getattr(getattr(self, "end", None), "date", None)
        if start and end:
            return f"{_fmt_date(start)}–{_fmt_date(end)}"
        if start:
            return _fmt_date(start)
        if end:
            return _fmt_date(end)
        return None

    def iso_string(self) -> str | None:
        start = getattr(getattr(self, "start", None), "date", None)
        end = getattr(getattr(self, "end", None), "date", None)
        if start or end:
            return f"{start or ''}/{end or ''}"
        return None


def parse_temporal(value: str) -> "ISO8601_2_Temporal":
    """Factory: parse *value* into ISO8601_2_Date or ISO8601_2_Period."""
    try:
        return ISO8601_2_Date(value)
    except (ValueError, AttributeError):
        pass
    try:
        return ISO8601_2_Period(value)
    except (ValueError, AttributeError):
        pass
    raise ValueError(f"Cannot parse as date or period: {value!r}")


class Variant(AttestableDatatype):
    """Contains a spell variant of a location name.
    The "@:" symbol splits the spell from its BCP47 language/dialect tag"""

    def _parse_value(self, value: str):
        if "@" not in value:
            value += "@"
        self.variant, self.lang_tag = value.split("@", maxsplit=1)


class PlaceOfEffect(AttestableDatatype):
    """The field describes a a place of effect of a person.
    It's split into a ISO_Temporal, LocationID, institution
    and occupation. The split symbol is ";".
    """

    def _parse_value(self, value: str):
        parts = value.split(";")
        if len(parts) != 4:
            raise ValueError(f"Expected 4 parts, got {len(parts)}: {value}")
        self.temporal, self.place, self.institution, self.occupation = parts
        self.temporal = parse_temporal(self.temporal)
        self.place = LocationID(self.place)
