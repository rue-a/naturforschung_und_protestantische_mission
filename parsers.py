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
    label: str
    parser: Callable | List[Callable]  # z.B. ID, ISO8601_2_Date, str
    is_list: bool = False
    codelist: Optional[list] = None  # the codelist
    require_source: bool = False


def flatten_parser_specs(
    spec_tree: dict, path: tuple[str, ...] = ()
) -> dict[str, tuple[tuple[str, ...], ParserSpec]]:
    flat_specs = {}

    for key, value in spec_tree.items():
        current_path = path + (key,)

        if isinstance(value, ParserSpec):
            flat_specs[value.label] = (current_path, value)
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
    "id": ParserSpec(label="ID", parser=ArchiveID),
    "name": ParserSpec(label="Name", parser=str),
    # --- Metadaten ---
    "abbreviations": ParserSpec(label="Abkürzungen", parser=str, is_list=True),
    # --- Link ---
    "link": ParserSpec(label="Link", parser=URL),
}

PARSERS_LITERATUR = {
    # --- Pflichtfelder ---
    "id": ParserSpec(label="ID", parser=LiteratureID),
    "title": ParserSpec(label="Titel", parser=str),
    # --- Links ---
    "permalink": ParserSpec(label="Permalink", parser=URL),
    # --- Freitext ---
    "description": ParserSpec(label="Beschreibung", parser=str),
}

PARSERS_MANUSKRIPTE = {
    # --- Pflichtfelder ---
    "id": ParserSpec(label="ID", parser=ManuscriptID),
    "archive": ParserSpec(label="Archiv", parser=ArchiveID),
    "signature": ParserSpec(label="Signatur", parser=str),
    "title": ParserSpec(label="Titel", parser=str),
    # --- Links ---
    "permalink": ParserSpec(label="Permalink", parser=URL),
    # --- Beschreibung ---
    "description": ParserSpec(label="Beschreibung", parser=str),
    # --- Identifiers ---
    "wikidata_id": ParserSpec(label="Wikidata ID", parser=str),
}

PARSERS_ORTE = {
    # --- Pflichtfelder ---
    "id": ParserSpec(label="ID", parser=LocationID),
    "name": ParserSpec(label="Name", parser=str),
    # --- Namensvarianten ---
    "variants": ParserSpec(
        label="Varianten",
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
        label="GeoNames-Typ",
        parser=str,
        is_list=True,
        codelist=["A", "H", "L", "P", "R", "S", "T"],
    ),
    "aat_type": ParserSpec(label="AAT-Typ", parser=int, is_list=True),
    # --- Zeitlicher Gültigkeitsbereich ---
    "start": ParserSpec(label="Beginn", parser=ISO8601_2_Date),
    "end": ParserSpec(label="Ende", parser=ISO8601_2_Date),
    # --- Authority Links ---
    "links": ParserSpec(label="Links", parser=URL, is_list=True),
    # --- Koordinaten ---
    "longitude": ParserSpec(label="Longitude", parser=float),
    "latitude": ParserSpec(label="Latitude", parser=float),
    # --- Geometrie ---
    "geometry": ParserSpec(label="Geometrie", parser=str),
    "geometry_source": ParserSpec(
        label="Geometriequelle", parser=[LiteratureID, ManuscriptID, URL]
    ),
    # --- Metadaten ---
    "location_accuracy": ParserSpec(label="Qualität der Ortsangabe", parser=str),
    "description": ParserSpec(label="Beschreibung", parser=str),
}

PARSERS_PERSONEN = {
    # --- Pflichtfelder ---
    "id": ParserSpec(label="ID", parser=PersonID),
    "include_in_person_lexicon": ParserSpec(
        label="Übernahme in Personenlexikon",
        parser=lambda v: {"ja": True, "nein": False}[clean_field(v).lower()],
    ),
    # --- Namen ---
    "name": {
        "preferred": ParserSpec(label="Name - Vorzugsname", parser=str),
        "surname": ParserSpec(label="Name - Nachname(n)", parser=str),
        "birth_name": ParserSpec(label="Name - Geburtsname(n)", parser=str),
        "given_name": ParserSpec(label="Name - Vorname(n)", parser=str),
        "title": ParserSpec(label="Name - Titel", parser=str),
        "notes": ParserSpec(label="Name - Anmerkungen", parser=str),
    },
    # --- Angehörige ---
    "relatives": {
        "siblings": ParserSpec(
            label="Angehörige - Geschwister", parser=PersonID, is_list=True
        ),
        "spouses": ParserSpec(
            label="Angehörige - Ehepartner", parser=PersonID, is_list=True
        ),
        "children": ParserSpec(
            label="Angehörige - Kinder", parser=PersonID, is_list=True
        ),
        "notes": ParserSpec(label="Angehörige - Anmerkungen", parser=str),
    },
    # --- Zugehörigkeit ---
    "member_of_moravians": ParserSpec(
        label="Zugehörigkeit Herrnhuter Brüdergemeine",
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
        "wikidata": ParserSpec(label="Links - Wikidata", parser=URL),
        "gnd": ParserSpec(label="Links - GND", parser=URL),
        "factgrid": ParserSpec(label="Links - FactGrid", parser=URL),
        "bionomia": ParserSpec(label="Links - Bionomia", parser=URL),
        "saebi": ParserSpec(label="Links - Säbi", parser=URL),
    },
    # --- Lebenslauf / IDs ---
    "moravian_curriculum_vitae": ParserSpec(
        label="Herrnhuter Lebenslauf", parser=[LiteratureID, ManuscriptID]
    ),
    # --- Geburt / Tod (structured!) ---
    "life": {
        "birth": {
            "date": ParserSpec(
                label="Geburt - Datum",
                parser=partial(ISO8601_2_Date, require_source=True),
                is_list=True,
            ),
            "date_notes": ParserSpec(label="Geburt - Datum - Anmerkungen", parser=str),
            "location": ParserSpec(
                label="Geburt - Ort",
                parser=partial(LocationID, require_source=True),
                is_list=True,
            ),
            "location_notes": ParserSpec(
                label="Geburt - Ort - Anmerkungen", parser=str
            ),
        },
        "death": {
            "date": ParserSpec(
                label="Tod - Datum",
                parser=partial(ISO8601_2_Date, require_source=True),
                is_list=True,
            ),
            "date_notes": ParserSpec(label="Tod - Datum - Anmerkungen", parser=str),
            "location": ParserSpec(
                label="Tod - Ort",
                parser=partial(LocationID, require_source=True),
                is_list=True,
            ),
            "location_notes": ParserSpec(label="Tod - Ort - Anmerkungen", parser=str),
        },
        # --- Wirkungsorte ---
        "places_of_effect": ParserSpec(
            label="Wirkungsorte",
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
            label="Tätigkeiten",
            parser=partial(AttestableString, require_source=True),
            is_list=True,
        ),
    },
    # --- Kontakte ---
    "contact": {
        "with_moravians": ParserSpec(
            label="Kontakt – Mit Herrnhutern",
            parser=partial(kontakt_parser, require_source=True),
            is_list=True,
        ),
        "with_non_moravians": ParserSpec(
            label="Kontakt – Mit Nicht-Herrnhutern",
            parser=partial(kontakt_parser, require_source=True),
            is_list=True,
        ),
    },
    # --- Botanik ---
    "botany": {
        "focuses": ParserSpec(label="Botanik - Foki", parser=str, is_list=True),
        "contribution_to_collections_object_evidence": ParserSpec(
            label="Botanik - Beitrag zu Sammlungen (Objektnachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_database_evidence": ParserSpec(
            label="Botanik - Beitrag zu Sammlungen (Datenbanknachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_literature_evidence": ParserSpec(
            label="Botanik - Beitrag zu Sammlungen (Literaturnachweis)",
            parser=partial(CollectionID, require_source=True),
            is_list=True,
        ),
        "contribution_to_collections_notes": ParserSpec(
            label="Botanik - Beitrag zu Sammlungen - Anmerkungen", parser=str
        ),
        "manuscripts_by_person": ParserSpec(
            label="Botanik - Manuskripte der Person",
            parser=ManuscriptID,
            is_list=True,
        ),
        "printed_works_by_person": ParserSpec(
            label="Botanik - Druckwerke der Person",
            parser=LiteratureID,
            is_list=True,
        ),
        "mentions_in_botanical_works_by_others": ParserSpec(
            label="Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere",
            parser=[LiteratureID, ManuscriptID],
            is_list=True,
        ),
    },
    "important_works_without_botanical_context": ParserSpec(
        label="Wichtige Werke der Person ohne botanischen Kontext",
        parser=[LiteratureID, ManuscriptID],
        is_list=True,
    ),
    "mentions_in_non_botanical_works_by_others": ParserSpec(
        label="Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere",
        parser=[LiteratureID, ManuscriptID],
        is_list=True,
    ),
}

PARSERS_SAMMLUNGEN = {
    # --- Pflichtfelder ---
    "id": ParserSpec(label="ID", parser=CollectionID),
    "collection_name": ParserSpec(label="Name der Sammlung", parser=str),
    # --- Metadaten ---
    "nybg_herbarium_code": ParserSpec(label="NYBG Herbarcode", parser=str),
    # --- Hierarchie ---
    "part_of_collection": ParserSpec(label="Teilsammlung von", parser=CollectionID),
    # --- Institution ---
    "holding_institution": ParserSpec(
        label="Sammlungshaltende Institution", parser=str, is_list=True
    ),
    # --- Links ---
    "website": ParserSpec(label="Webseite", parser=URL),
    # --- Freitext ---
    "notes": ParserSpec(label="Anmerkungen", parser=str),
}
