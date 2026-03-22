from dataclasses import dataclass
from typing import Callable, Optional, List
from functools import partial
import re

from new_datatypes import (
    PersonID,
    LiteratureID,
    LocationID,
    ManuscriptID,
    ArchiveID,
    CollectionID,
    URL,
    AttestableString,
    ISO_Date,
    ISO8601_2_Date,
    ISO8601_2_Period,
    ISO8601_2_Temporal,
    ComplexType,
)


@dataclass(frozen=True)
class ParserSpec:
    excel_column_name: str
    parser: Callable | List[Callable]  # z.B. ID, ISO8601_2_Date, str
    label: Optional[str] = None
    is_list: bool = False
    codelist: Optional[list] = None  # the codelist
    require_source: bool = False

    def __post_init__(self):
        if self.label is None:
            object.__setattr__(self, "label", self.excel_column_name)


def flatten_parser_specs(
    spec_tree: dict, path: tuple[str, ...] = ()
) -> dict[str, tuple[tuple[str, ...], ParserSpec]]:
    flat_specs = {}

    for key, value in spec_tree.items():
        current_path = path + (key,)

        if isinstance(value, ParserSpec):
            flat_specs[value.excel_column_name] = (current_path, value)
            continue

        if isinstance(value, dict):
            flat_specs.update(flatten_parser_specs(value, current_path))
            continue

        raise TypeError(
            f"Unsupported parser spec node at {current_path}: {type(value)!r}"
        )

    return flat_specs


def clean_field(raw: str) -> str:
    """Normalize field before parsing:
    - Remove all newlines
    - Remove all spaces around '|'
    - Collapse multiple spaces elsewhere into one
    - Trim leading/trailing spaces
    """
    if not raw:
        return ""

    # remove all newlines
    raw = raw.replace("\n", "")

    # remove square brackets and their content
    raw = re.sub(r"\[.*?\]", "", raw)

    # remove all spaces around pipes
    raw = re.sub(r"\s*\|\s*", "|", raw)

    # collapse multiple spaces elsewhere
    raw = re.sub(r"\s+", " ", raw)

    # strip leading/trailing spaces
    raw = raw.strip()

    # print(f"cleaned: {raw}")

    return raw


def parse_field(
    cleaned_raw: str,
    parser: Callable | List[Callable],
    is_list: bool = False,
    codelist: List[str] = [],
):

    def parse_one(value: str):

        # codelist validation
        if codelist:
            if value not in codelist:
                raise ValueError(f"{value!r} not in codelist")

        # Single parser
        if callable(parser):
            return parser(value)

        # Multiple parsers (fallback chain)
        last_error = None
        for p in parser:
            try:
                return p(value)
            except Exception as e:
                last_error = e

        raise ValueError("No parser accepted value!") from last_error

    if is_list:
        if not cleaned_raw:
            return []
        return [parse_one(v) for v in cleaned_raw.split("|")]

    return parse_one(cleaned_raw)


kontakt_parser = ComplexType(
    parts=[
        PersonID,  # 0: P-ID (required)
        ISO8601_2_Temporal,  # 1: optional temporal
    ],
    separator=";",  # separator between P-ID and temporal
)


PARSERS_ARCHIVE = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=ArchiveID),
    "name": ParserSpec(excel_column_name="Name", parser=str),
    # --- Metadaten ---
    "abbreviations": ParserSpec(
        excel_column_name="Abkürzungen", parser=str, is_list=True
    ),
    # --- Link ---
    "link": ParserSpec(excel_column_name="Link", parser=URL),
}

PARSERS_LITERATUR = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=LiteratureID),
    "title": ParserSpec(excel_column_name="Titel", parser=str),
    # --- Links ---
    "permalink": ParserSpec(excel_column_name="Permalink", parser=URL),
    # --- Freitext ---
    "description": ParserSpec(excel_column_name="Beschreibung", parser=str),
}

PARSERS_MANUSKRIPTE = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=ManuscriptID),
    "archive": ParserSpec(excel_column_name="Archiv", parser=ArchiveID),
    "signature": ParserSpec(excel_column_name="Signatur", parser=str),
    "title": ParserSpec(excel_column_name="Titel", parser=str),
    # --- Links ---
    "permalink": ParserSpec(excel_column_name="Permalink", parser=URL),
    # --- Beschreibung ---
    "description": ParserSpec(excel_column_name="Beschreibung", parser=str),
    # --- Identifiers ---
    "wikidata_id": ParserSpec(excel_column_name="Wikidata ID", parser=str),
}

PARSERS_ORTE = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=LocationID),
    "name": ParserSpec(excel_column_name="Name", parser=str),
    # --- Namensvarianten ---
    "variants": ParserSpec(
        excel_column_name="Varianten",
        parser=ComplexType(
            parts=[
                str,  # name
                str,  # BCP47 language tag
            ],
            separator="@",
        ),
        is_list=True,
    ),
    # --- Typklassifikation ---
    "geonames_type": ParserSpec(
        excel_column_name="GeoNames-Typ",
        parser=str,
        is_list=True,
        codelist=["A", "H", "L", "P", "R", "S", "T"],
    ),
    "aat_type": ParserSpec(excel_column_name="AAT-Typ", parser=int, is_list=True),
    # --- Zeitlicher Gültigkeitsbereich ---
    "start": ParserSpec(excel_column_name="Beginn", parser=ISO8601_2_Date),
    "end": ParserSpec(excel_column_name="Ende", parser=ISO8601_2_Date),
    # --- Authority Links ---
    "links": ParserSpec(excel_column_name="Links", parser=URL, is_list=True),
    # --- Koordinaten ---
    "longitude": ParserSpec(excel_column_name="Longitude", parser=float),
    "latitude": ParserSpec(excel_column_name="Latitude", parser=float),
    # --- Geometrie ---
    "geometry": ParserSpec(excel_column_name="Geometrie", parser=str),
    "geometry_source": ParserSpec(
        excel_column_name="Geometriequelle",
        parser=[LiteratureID, ManuscriptID, URL],
    ),
    # --- Metadaten ---
    "location_accuracy": ParserSpec(
        excel_column_name="Qualität der Ortsangabe", parser=str
    ),
    "description": ParserSpec(excel_column_name="Beschreibung", parser=str),
}

PARSERS_PERSONEN = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=PersonID),
    "include_in_person_lexicon": ParserSpec(
        excel_column_name="Übernahme in Personenlexikon",
        parser=lambda v: {"ja": True, "nein": False}[clean_field(v).lower()],
    ),
    # --- Namen ---
    "name": {
        "preferred": ParserSpec(excel_column_name="Name - Vorzugsname", parser=str),
        "surname": ParserSpec(excel_column_name="Name - Nachname(n)", parser=str),
        "birth_name": ParserSpec(excel_column_name="Name - Geburtsname(n)", parser=str),
        "given_name": ParserSpec(excel_column_name="Name - Vorname(n)", parser=str),
        "title": ParserSpec(excel_column_name="Name - Titel", parser=str),
        "notes": ParserSpec(excel_column_name="Name - Anmerkungen", parser=str),
    },
    # --- Angehörige ---
    "relatives": {
        "siblings": ParserSpec(
            excel_column_name="Angehörige - Geschwister",
            parser=PersonID,
            is_list=True,
        ),
        "spouses": ParserSpec(
            excel_column_name="Angehörige - Ehepartner",
            parser=PersonID,
            is_list=True,
        ),
        "children": ParserSpec(
            excel_column_name="Angehörige - Kinder",
            parser=PersonID,
            is_list=True,
        ),
        "notes": ParserSpec(excel_column_name="Angehörige - Anmerkungen", parser=str),
    },
    # --- Zugehörigkeit ---
    "member_of_moravians": ParserSpec(
        excel_column_name="Zugehörigkeit Herrnhuter Brüdergemeine",
        parser=str,
        is_list=True,
        codelist=[
            "ja(a)",
            "ja(b)",
            "ja(c)",
            "ja(d)",
            "nein(a)",
            "nein(b)",
            "nein(c)",
            "unbekannt",
        ],
    ),
    # --- Links ---
    "links": {
        "wikidata": ParserSpec(
            excel_column_name="Links - Wikidata", label="Wikidata", parser=URL
        ),
        "gnd": ParserSpec(excel_column_name="Links - GND", label="GND", parser=URL),
        "factgrid": ParserSpec(
            excel_column_name="Links - FactGrid", label="FactGrid", parser=URL
        ),
        "bionomia": ParserSpec(
            excel_column_name="Links - Bionomia", label="Bionomia", parser=URL
        ),
        "saebi": ParserSpec(
            excel_column_name="Links - Säbi", label="Sächsische Biografie", parser=URL
        ),
    },
    # --- Lebenslauf / IDs ---
    "moravian_curriculum_vitae": ParserSpec(
        excel_column_name="Herrnhuter Lebenslauf",
        parser=[LiteratureID, ManuscriptID],
    ),
    # --- Geburt / Tod (structured!) ---
    "life": {
        "birth": {
            "date": ParserSpec(
                excel_column_name="Geburt - Datum",
                parser=partial(ISO8601_2_Date, require_source=True),
                is_list=True,
            ),
            "date_notes": ParserSpec(
                excel_column_name="Geburt - Datum - Anmerkungen",
                parser=str,
            ),
            "location": ParserSpec(
                excel_column_name="Geburt - Ort",
                parser=partial(LocationID, require_source=True),
                is_list=True,
            ),
            "location_notes": ParserSpec(
                excel_column_name="Geburt - Ort - Anmerkungen",
                parser=str,
            ),
        },
        "death": {
            "date": ParserSpec(
                excel_column_name="Tod - Datum",
                parser=partial(ISO8601_2_Date, require_source=True),
                is_list=True,
            ),
            "date_notes": ParserSpec(
                excel_column_name="Tod - Datum - Anmerkungen",
                parser=str,
            ),
            "location": ParserSpec(
                excel_column_name="Tod - Ort",
                parser=partial(LocationID, require_source=True),
                is_list=True,
            ),
            "location_notes": ParserSpec(
                excel_column_name="Tod - Ort - Anmerkungen",
                parser=str,
            ),
        },
        # --- Wirkungsorte ---
        "places_of_effect": ParserSpec(
            excel_column_name="Wirkungsorte",
            parser=ComplexType(
                parts=[
                    ISO8601_2_Temporal,  # Zeitraum
                    LocationID,  # Ort (must be L-ID)
                    str,  # Einrichtung
                    str,  # Funktion
                ],
            ),
            is_list=True,
        ),
        # --- Tätigkeiten ---
        "activities": ParserSpec(
            excel_column_name="Tätigkeiten",
            parser=partial(AttestableString, require_source=True),
            is_list=True,
        ),
    },
    # --- Kontakte ---
    "contact": {
        "with_moravians": ParserSpec(
            excel_column_name="Kontakt – Mit Herrnhutern",
            parser=partial(kontakt_parser, require_source=True),
            is_list=True,
        ),
        "with_non_moravians": ParserSpec(
            excel_column_name="Kontakt – Mit Nicht-Herrnhutern",
            parser=partial(kontakt_parser, require_source=True),
            is_list=True,
        ),
    },
    # --- Botanik ---
    "botany": {
        "focuses": ParserSpec(
            excel_column_name="Botanik - Foki", parser=str, is_list=True
        ),
        "contribution_to_collections_object_evidence": ParserSpec(
            excel_column_name="Botanik - Beitrag zu Sammlungen (Objektnachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_database_evidence": ParserSpec(
            excel_column_name="Botanik - Beitrag zu Sammlungen (Datenbanknachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_literature_evidence": ParserSpec(
            excel_column_name="Botanik - Beitrag zu Sammlungen (Literaturnachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_notes": ParserSpec(
            excel_column_name="Botanik - Beitrag zu Sammlungen - Anmerkungen",
            parser=str,
        ),
        "manuscripts_by_person": ParserSpec(
            excel_column_name="Botanik - Manuskripte der Person",
            parser=ManuscriptID,
            is_list=True,
        ),
        "printed_works_by_person": ParserSpec(
            excel_column_name="Botanik - Druckwerke der Person",
            parser=LiteratureID,
            is_list=True,
        ),
        "mentions_in_botanical_works_by_others": ParserSpec(
            excel_column_name="Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere",
            parser=[LiteratureID, ManuscriptID],
            is_list=True,
        ),
    },
    "important_works_without_botanical_context": ParserSpec(
        excel_column_name="Wichtige Werke der Person ohne botanischen Kontext",
        parser=[LiteratureID, ManuscriptID],
        is_list=True,
    ),
    "mentions_in_non_botanical_works_by_others": ParserSpec(
        excel_column_name="Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere",
        parser=[LiteratureID, ManuscriptID],
        is_list=True,
    ),
}

PARSERS_SAMMLUNGEN = {
    # --- Pflichtfelder ---
    "id": ParserSpec(excel_column_name="ID", parser=CollectionID),
    "collection_name": ParserSpec(excel_column_name="Name der Sammlung", parser=str),
    # --- Metadaten ---
    "nybg_herbarium_code": ParserSpec(excel_column_name="NYBG Herbarcode", parser=str),
    # --- Hierarchie ---
    "part_of_collection": ParserSpec(
        excel_column_name="Teilsammlung von", parser=CollectionID
    ),
    # --- Institution ---
    "holding_institution": ParserSpec(
        excel_column_name="Sammlungshaltende Institution",
        parser=str,
        is_list=True,
    ),
    # --- Links ---
    "website": ParserSpec(excel_column_name="Webseite", parser=URL),
    # --- Freitext ---
    "notes": ParserSpec(excel_column_name="Anmerkungen", parser=str),
}
