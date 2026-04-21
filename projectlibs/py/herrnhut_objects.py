from abc import ABC, abstractmethod
from types import SimpleNamespace
from typing import Callable
from projectlibs.py.field_datatypes import (
    AttestableDatatype,
    String,
    EncodedString,
    URL,
    ISO8601_2_Date,
    PlaceOfEffect,
    Variant,
    PersonID,
    LocationID,
    CollectionID,
    ManuscriptID,
    LiteratureID,
    ArchiveID,
    WorkID,
)


class HerrnhutObject(ABC):
    @abstractmethod
    def _parse_input(self, raw_input: dict):
        pass

    @abstractmethod
    def enrich(self):
        pass

    @abstractmethod
    def serialize_json(self):
        pass

    def __init__(self, raw_input: dict):
        self._parse_input(raw_input)


def parse_list_field(field: str, parser: Callable) -> list:
    return [parser(el) for el in field.split("|")]


class HerrnhutPerson(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = PersonID(input_data["ID"])

        self.hidden = EncodedString(
            input_data["Übernahme in Personenlexikon"],
            codelist={"ja": True, "nein": False},
        )

        self.name = SimpleNamespace()
        self.name.preferred = String(input_data["Name - Vorzugsname"])
        self.name.surname = String(input_data["Name - Nachname(n)"])
        self.name.birth_name = String(input_data["Name - Geburtsname(n)"])
        self.name.given_name = String(input_data["Name - Vorname(n)"])
        self.name.title = String(input_data["Name - Titel"])
        self.name.notes = String(input_data["Name - Anmerkungen"])

        self.relatives = SimpleNamespace()
        self.relatives.siblings = parse_list_field(
            input_data["Angehörige - Geschwister"], PersonID
        )
        self.relatives.spouses = parse_list_field(
            input_data["Angehörige - Ehepartner"], PersonID
        )
        self.relatives.children = parse_list_field(
            input_data["Angehörige - Kinder"], PersonID
        )
        self.relatives.notes = String(input_data["Angehörige - Anmerkungen"])
        self.links = SimpleNamespace()
        self.links.wikidata = URL(input_data["Links - Wikidata"])
        self.links.gnd = URL(input_data["Links - GND"])
        self.links.factgrid = URL(input_data["Links - FactGrid"])
        self.links.bionomia = URL(input_data["Links - Bionomia"])
        self.links.saebi = URL(input_data["Links - Säbi"])

        self.member_of_moravians = EncodedString(
            input_data["Zugehörigkeit Herrnhuter Brüdergemeine"],
            codelist={
                "ja(a)": "qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen",
                "ja(b)": "als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte",
                "ja(c)": "Übernahme von kirchlichen Ämtern innerhalb der Brüdergemeine",
                "ja(d)": "Übernahme von Ämtern im Erziehungswesen der Brüdergemeine",
                "nein(a)": "ausgetreten",
                "nein(b)": "aber wichtig im Netzwerk",
                "nein(c)": "um Verwechslung auszuschließen",
                "unbekannt": "Zugehörigkeit kann nicht ausgeschlossen werden.",
            },
        )

        self.birth = SimpleNamespace()
        self.birth.date = ISO8601_2_Date(
            input_data["Geburt - Datum"], require_source=True
        )
        self.birth.date_notes = String(input_data["Geburt - Datum - Anmerkungen"])
        self.birth.location = LocationID(
            input_data["Geburt - Ort"], require_source=True
        )
        self.birth.location_notes = String(input_data["Geburt - Ort - Anmerkungen"])

        self.death = SimpleNamespace()
        self.death.date = ISO8601_2_Date(input_data["Tod - Datum"], require_source=True)
        self.death.date_notes = String(input_data["Tod - Datum - Anmerkungen"])
        self.death.location = LocationID(input_data["Tod - Ort"], require_source=True)
        self.death.location_notes = String(input_data["Tod - Ort - Anmerkungen"])

        self.places_of_effect = parse_list_field(
            input_data["Wirkungsorte"], PlaceOfEffect
        )

        self.moravian_curriculum_vitae = WorkID(input_data["Herrnhuter Lebenslauf"])

        self.contact = SimpleNamespace()
        self.contact.with_moravians = parse_list_field(
            input_data["Kontakt - Mit Herrnhutern"],
            lambda v: PersonID(v, require_source=True),
        )
        self.contact.with_non_moravians = parse_list_field(
            input_data["Kontakt - Mit Nicht-Herrnhutern"],
            lambda v: PersonID(v, require_source=True),
        )

        self.botany = SimpleNamespace()
        self.botany.focuses = parse_list_field(input_data["Botanik - Foki"], String)

        self.botany.contribution_to_collections = SimpleNamespace()
        self.botany.contribution_to_collections.object_evidence = parse_list_field(
            input_data["Botanik - Beitrag zu Sammlungen (Objektnachweis)"],
            lambda v: CollectionID(v, require_source=True),
        )
        self.botany.contribution_to_collections.database_evidence = parse_list_field(
            input_data["Botanik - Beitrag zu Sammlungen (Datenbanknachweis)"],
            lambda v: CollectionID(v, require_source=True),
        )
        self.botany.contribution_to_collections.literature_evidence = parse_list_field(
            input_data["Botanik - Beitrag zu Sammlungen (Literaturnachweis)"],
            lambda v: CollectionID(v, require_source=True),
        )
        self.botany.contribution_to_collections.notes = String(
            input_data["Botanik - Beitrag zu Sammlungen - Anmerkungen"]
        )

        self.botany.works = SimpleNamespace()
        self.botany.works.manuscripts = parse_list_field(
            input_data["Botanik - Manuskripte der Person"], ManuscriptID
        )
        self.botany.works.printed = parse_list_field(
            input_data["Botanik - Druckwerke der Person"], LiteratureID
        )

        self.botany.citations = SimpleNamespace()
        self.botany.citations.in_botanical_works_by_others = parse_list_field(
            input_data[
                "Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere"
            ],
            WorkID,
        )

        self.works = SimpleNamespace()
        self.works.without_botanical_context = parse_list_field(
            input_data["Wichtige Werke der Person ohne botanischen Kontext"],
            WorkID,
        )

        self.citations = SimpleNamespace()
        self.citations.in_non_botanical_works_by_others = parse_list_field(
            input_data[
                "Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere"
            ],
            WorkID,
        )

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutArchive(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = ArchiveID(input_data["ID"])
        self.name = String(input_data["Name"])
        self.abbreviations = parse_list_field(input_data["Abkürzungen"], String)
        self.link = URL(input_data["Link"])

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutManuscript(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = ManuscriptID(input_data["ID"])
        self.archive = ArchiveID(input_data["Archiv"])
        self.signature = String(input_data["Signatur"])
        self.title = String(input_data["Titel"])
        self.permalink = URL(input_data["Permalink"])
        self.description = String(input_data["Beschreibung"])
        self.wikidata_id = String(input_data["Wikidata ID"])

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutLiterature(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = LiteratureID(input_data["ID"])
        self.title = String(input_data["Titel"])
        self.permalink = URL(input_data["Permalink"])
        self.description = String(input_data["Beschreibung"])

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutLocation(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = LocationID(input_data["ID"])
        self.name = String(input_data["Name"])
        self.variants = parse_list_field(input_data["Varianten"], Variant)
        self.wikidata = URL(input_data["Wikidata"])
        self.description = String(input_data["Beschreibung"])

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutCollection(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = CollectionID(input_data["ID"])
        self.nybg_herbarium_code = String(input_data["NYBG Herbarcode"])
        self.name = String(input_data["Name der Sammlung"])
        self.part_of_collection = CollectionID(input_data["Teilsammlung von"])
        self.holding_institutions = parse_list_field(
            input_data["Sammlungshaltende Institution"], String
        )
        self.website = URL(input_data["Webseite"])
        self.notes = String(input_data["Anmerkungen"])

    def enrich(self):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError
