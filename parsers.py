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
    parser: Callable | List[Callable]  # z.B. ID, ISO8601_2_Date, str
    is_list: bool = False
    codelist: Optional[list] = None  # the codelist
    require_source: bool = False


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


CODELISTS = {
    "member_of_moravians": [
        "ja(a)",
        "ja(b)",
        "ja(c)",
        "ja(d)",
        "nein(a)",
        "nein(b)",
        "nein(c)",
        "unbekannt",
    ]
}

kontakt_parser = ComplexType(
    parts=[
        PersonID,  # 0: P-ID (required)
        ISO8601_2_Temporal,  # 1: optional temporal
    ],
    separator=";",  # separator between P-ID and temporal
)


PARSERS_ARCHIVE = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=ArchiveID),
    "Name": ParserSpec(parser=str),
    # --- Metadaten ---
    "Abkürzungen": ParserSpec(parser=str, is_list=True),
    # --- Link ---
    "Link": ParserSpec(parser=URL),
}

PARSERS_LITERATUR = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=LiteratureID),
    "Titel": ParserSpec(parser=str),
    # --- Links ---
    "Permalink": ParserSpec(parser=URL),
    # --- Freitext ---
    "Beschreibung": ParserSpec(parser=str),
}

PARSERS_MANUSKRIPTE = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=ManuscriptID),
    "Archiv": ParserSpec(parser=ArchiveID),
    "Signatur": ParserSpec(parser=str),
    "Titel": ParserSpec(parser=str),
    # --- Links ---
    "Permalink": ParserSpec(parser=URL),
    # --- Beschreibung ---
    "Beschreibung": ParserSpec(parser=str),
    # --- Identifiers ---
    "Wikidata ID": ParserSpec(parser=str),
}

PARSERS_ORTE = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=LocationID),
    "Name": ParserSpec(parser=str),
    # --- Namensvarianten ---
    "Varianten": ParserSpec(
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
    "GeoNames-Typ": ParserSpec(
        parser=str,
        is_list=True,
        codelist=["A", "H", "L", "P", "R", "S", "T"],
    ),
    "AAT-Typ": ParserSpec(parser=int, is_list=True),
    # --- Zeitlicher Gültigkeitsbereich ---
    "Beginn": ParserSpec(parser=ISO8601_2_Date),
    "Ende": ParserSpec(parser=ISO8601_2_Date),
    # --- Authority Links ---
    "Links": ParserSpec(parser=URL, is_list=True),
    # --- Koordinaten ---
    "Longitude": ParserSpec(parser=float),
    "Latitude": ParserSpec(parser=float),
    # --- Geometrie ---
    "Geometrie": ParserSpec(parser=str),
    "Geometriequelle": ParserSpec(parser=[LiteratureID, ManuscriptID, URL]),
    # --- Metadaten ---
    "Qualität der Ortsangabe": ParserSpec(parser=str),
    "Beschreibung": ParserSpec(parser=str),
}

PARSERS_PERSONEN = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=PersonID),
    "Übernahme in Personenlexikon": ParserSpec(
        parser=lambda v: {"ja": True, "nein": False}[clean_field(v).lower()]
    ),
    "Name - Vorzugsname": ParserSpec(parser=str),
    # --- Namen ---
    "Name - Nachname(n)": ParserSpec(parser=str),
    "Name - Geburtsname(n)": ParserSpec(parser=str),
    "Name - Vorname(n)": ParserSpec(parser=str),
    "Name - Titel": ParserSpec(parser=str),
    "Name - Anmerkungen": ParserSpec(parser=str),
    # --- Angehörige ---
    "Angehörige - Geschwister": ParserSpec(parser=PersonID, is_list=True),
    "Angehörige - Ehepartner": ParserSpec(parser=PersonID, is_list=True),
    "Angehörige - Kinder": ParserSpec(parser=PersonID, is_list=True),
    "Angehörige - Anmerkungen": ParserSpec(parser=str),
    # --- Zugehörigkeit ---
    "Zugehörigkeit Herrnhuter Brüdergemeine": ParserSpec(
        parser=str, is_list=True, codelist=CODELISTS["member_of_moravians"]
    ),
    # --- Links ---
    "Links - Wikidata": ParserSpec(parser=URL),
    "Links - GND": ParserSpec(parser=URL),
    "Links - FactGrid": ParserSpec(parser=URL),
    "Links - Bionomia": ParserSpec(parser=URL),
    "Links - Säbi": ParserSpec(parser=URL),
    # --- Lebenslauf / IDs ---
    "Herrnhuter Lebenslauf": ParserSpec(parser=[LiteratureID, ManuscriptID]),
    # --- Geburt / Tod (structured!) ---
    "Geburt - Datum": ParserSpec(
        parser=partial(ISO8601_2_Date, require_source=True), is_list=True
    ),
    "Geburt - Datum - Anmerkungen": ParserSpec(parser=str),
    "Geburt - Ort": ParserSpec(
        parser=partial(LocationID, require_source=True), is_list=True
    ),
    "Geburt - Ort - Anmerkungen": ParserSpec(parser=str),
    "Tod - Datum": ParserSpec(
        parser=partial(ISO8601_2_Date, require_source=True), is_list=True
    ),
    "Tod - Datum - Anmerkungen": ParserSpec(parser=str),
    "Tod - Ort": ParserSpec(
        parser=partial(LocationID, require_source=True), is_list=True
    ),
    "Tod - Ort - Anmerkungen": ParserSpec(parser=str),
    # --- Wirkungsorte ---
    "Wirkungsorte": ParserSpec(
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
    "Tätigkeiten": ParserSpec(
        parser=partial(AttestableString, require_source=True), is_list=True
    ),
    # --- Kontakte ---
    # --- ParserSpec entries ---
    "Kontakt – Mit Herrnhutern": ParserSpec(
        parser=partial(kontakt_parser, require_source=True),
        is_list=True,
    ),
    "Kontakt – Mit Nicht-Herrnhutern": ParserSpec(
        parser=partial(kontakt_parser, require_source=True),
        is_list=True,
    ),
    # --- Botanik ---
    "Botanik - Foki": ParserSpec(parser=str, is_list=True),
    "Botanik - Beitrag zu Sammlungen (Objektnachweis)": ParserSpec(
        parser=partial(CollectionID, require_source=True), is_list=True
    ),
    "Botanik - Beitrag zu Sammlungen (Datenbanknachweis)": ParserSpec(
        parser=partial(CollectionID, require_source=True), is_list=True
    ),
    "Botanik - Beitrag zu Sammlungen (Literaturnachweis)": ParserSpec(
        parser=partial(CollectionID, require_source=True), is_list=True
    ),
    "Botanik - Beitrag zu Sammlungen - Anmerkungen": ParserSpec(parser=str),
    "Botanik - Manuskripte der Person": ParserSpec(parser=ManuscriptID, is_list=True),
    "Botanik - Druckwerke der Person": ParserSpec(parser=LiteratureID, is_list=True),
    "Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere": ParserSpec(
        parser=[LiteratureID, ManuscriptID], is_list=True
    ),
    "Wichtige Werke der Person ohne botanischen Kontext": ParserSpec(
        parser=[LiteratureID, ManuscriptID], is_list=True
    ),
    "Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere": ParserSpec(
        parser=[LiteratureID, ManuscriptID], is_list=True
    ),
}

PARSERS_SAMMLUNGEN = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=CollectionID),
    "Name der Sammlung": ParserSpec(parser=str),
    # --- Metadaten ---
    "NYBG Herbarcode": ParserSpec(parser=str),
    # --- Hierarchie ---
    "Teilsammlung von": ParserSpec(parser=CollectionID),
    # --- Institution ---
    "Sammlungshaltende Institution": ParserSpec(parser=str, is_list=True),
    # --- Links ---
    "Webseite": ParserSpec(parser=URL),
    # --- Freitext ---
    "Anmerkungen": ParserSpec(parser=str),
}
