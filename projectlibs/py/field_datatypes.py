import re
from abc import ABC, abstractmethod
from validators import url


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
        # get string in parantheses
        source_pattern = re.compile(r"^(.*?)\s*\((.*?)\)$")

        match = source_pattern.fullmatch(in_string)
        if match:
            value, source = match.groups()
            if require_source and not source:
                raise ValueError(
                    f"Statement ({in_string}) requires attestation (no source was provided)!"
                )
            return value, source

        return in_string, None

    def __init__(self, raw: str, require_source=False):

        raw = clean_field(raw)
        if not raw:
            return None
        self.raw = raw
        value, source_string = self._split_value_and_source(raw, require_source)
        if source_string:
            self.source = ReferenceDocument(source_string, require_source=False)
        else:
            self.source = None
        self._parse_value(value)

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


class ISO8601_2_Date(AttestableDatatype):
    """Day- to year-level ISO8601-2 date"""

    def _parse_value(self, value: str):
        pattern = r"^(\d{4})(-\d{2})?(-\d{2})?([~%?])?$"
        if not re.fullmatch(pattern, value):
            raise ValueError(f"Invalid ISO8601-2_Date format: {value}")


class ISO8601_2_Period(AttestableDatatype):
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


class ISO8601_2_Temporal(AttestableDatatype):
    """Contains ISO8601-2_Date or ISO8601-2_Period"""

    def _parse_value(self, value: str):
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

        raise ValueError(f"Invalid Temporal value: {value}")


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
