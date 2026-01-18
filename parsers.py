from dataclasses import dataclass
from typing import Callable, Optional
import re

from new_datatypes import (
    ID,
    URL,
    ISO_Date,
    ISO8601_2_Date,
    ISO8601_2_Period,
    ISO8601_2_Temporal,
    ComplexType,
)


@dataclass(frozen=True)
class ParserSpec:
    parser: Callable  # z.B. ID, ISO8601_2_Date, str
    is_list: bool = False
    codelist: Optional[list] = None  # the codelist


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

    return raw


def parse_field(
    raw: str,
    *,
    parser,
    is_list: bool = False,
    codelist: set[str] | None = None,
):
    raw = clean_field(raw)  # <<< CLEAN BEFORE PARSING

    def parse_one(value: str):
        if codelist is not None:
            if value not in codelist:
                raise ValueError(f"{value!r} not in codelist")
        return parser(value)

    if is_list:
        if not raw:
            return []
        return [parse_one(v) for v in raw.split("|")]

    return parse_one(raw)


CODELISTS = {
    "member_of_moravians": {
        "ja(a)",
        "ja(b)",
        "ja(c)",
        "ja(d)",
        "nein(a)",
        "nein(b)",
        "nein(c)",
        "unbekannt",
    }
}

kontakt_parser = ComplexType(
    parts=[
        ID,  # 0: P-ID (required)
        ISO8601_2_Temporal,  # 1: optional temporal
    ],
    separator=";",  # separator between P-ID and temporal
    validators={
        0: lambda v: (
            None
            if isinstance(v, ID) and v.type == "person"
            else (_ for _ in ()).throw(
                ValueError(f"Expected P-ID (person), got {v.value!r}")
            )
        ),
    },
)

PARSERS_PERSONEN = {
    # --- Pflichtfelder ---
    "ID": ParserSpec(parser=ID),
    "Übernahme in Personenlexikon": ParserSpec(
        parser=lambda v: ({"ja": True, "nein": False}[clean_field(v).lower()])
    ),
    "Name - Vorzugsname": ParserSpec(parser=str),
    # --- Namen ---
    "Name - Nachname(n)": ParserSpec(parser=str),
    "Name - Geburtsname(n)": ParserSpec(parser=str),
    "Name - Vornamen(n)": ParserSpec(parser=str),
    "Name - Titel": ParserSpec(parser=str),
    "Name - Anmerkungen": ParserSpec(parser=str),
    # --- Angehörige ---
    "Angehörige - Geschwister": ParserSpec(parser=ID, is_list=True),
    "Angehörige - Ehepartner": ParserSpec(parser=ID, is_list=True),
    "Angehörige - Kinder": ParserSpec(parser=ID, is_list=True),
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
    "Handschriftlicher Lebenslauf": ParserSpec(parser=ID),
    # --- Geburt / Tod (structured!) ---
    "Geburt - Datum": ParserSpec(parser=ISO8601_2_Date, is_list=True),
    "Geburt - Ort": ParserSpec(parser=ID, is_list=True),  # L-ID
    "Tod - Datum": ParserSpec(parser=ISO8601_2_Date, is_list=True),
    "Tod - Ort": ParserSpec(parser=ID, is_list=True),  # L-ID
    # --- Wirkungsorte ---
    # --- Wirkungsorte ---
    "Wirkungsorte": ParserSpec(
        parser=ComplexType(
            parts=[
                ISO8601_2_Temporal,  # Zeitraum
                ID,  # Ort (must be L-ID)
                str,  # Einrichtung
                str,  # Funktion
            ],
            validators={
                1: lambda v: (
                    None
                    if isinstance(v, ID) and v.type == "location"
                    else (_ for _ in ()).throw(
                        ValueError(f"Expected L-ID (location), got {v.value!r}")
                    )
                ),
            },
        ),
        is_list=True,
    ),
    # --- Tätigkeiten ---
    "Tätigkeiten": ParserSpec(parser=str, is_list=True),
    # --- Kontakte ---
    # --- ParserSpec entries ---
    "KONTAKT – Mit Herrnhutern": ParserSpec(
        parser=kontakt_parser,
        is_list=True,
    ),
    "KONTAKT – Mit Nicht-Herrnhutern": ParserSpec(
        parser=kontakt_parser,
        is_list=True,
    ),
    # --- Botanik ---
    "Botanik - Foki": ParserSpec(parser=str, is_list=True),
    "Botanik - Manuskripte der Person": ParserSpec(parser=ID, is_list=True),
    "Botanik - Druckwerke der Person": ParserSpec(parser=ID, is_list=True),
    "Botanik - Erwähnung der Person in Manuskripten durch Andere": ParserSpec(
        parser=ID, is_list=True
    ),
    "Botanik - Erwähnung der Person in Druckwerken durch Andere": ParserSpec(
        parser=ID, is_list=True
    ),
    "Wichtige Werke der Person ohne botanischen Kontext": ParserSpec(
        parser=ID, is_list=True
    ),
    "Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere": ParserSpec(
        parser=ID, is_list=True
    ),
}


#
# CODELISTS = {
#     "Nadelbäume": {"Fichte", "Tanne", "Kiefer", "Lärche"},
# }
# # default
# print(parse_field("2025-01-15", parser=ISO_Date))

# # list
# print(
#     parse_field(
#         "2025-01-15 | 2026-01-01",
#         parser=ISO_Date,
#         is_list=True,
#     )
# )

# # from codelist
# print(
#     parse_field(
#         "Fichte",
#         parser=str,
#         codelist=CODELISTS["Nadelbäume"],
#     )
# )

# # list from codelist
# print(
#     parse_field(
#         "Fichte | Tanne",
#         parser=str,
#         is_list=True,
#         codelist=CODELISTS["Nadelbäume"],
#     )
# )
