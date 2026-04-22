from abc import ABC, abstractmethod
import warnings
from functools import partial
from types import SimpleNamespace

from projectlibs.py.field_datatypes import (
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
from projectlibs.py.helpers.wikidata_utils import (
    fetch_person_data_from_wikipedia,
    fetch_location_data_from_wikidata,
)


class HerrnhutObject(ABC):
    @abstractmethod
    def _parse_input(self, raw_input: dict):
        pass

    @abstractmethod
    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        pass

    @abstractmethod
    def serialize_json(self):
        pass

    def __init__(self, raw_input: dict):
        self._errors: list[
            tuple[str, str, str, str]
        ] = []  # (column, causing, full_raw, message)
        self._parse_input(raw_input)

    def _parse_field(self, column: str, raw: str, constructor) -> object:
        try:
            return constructor(raw)
        except (ValueError, KeyError) as e:
            self._errors.append((column, raw, raw, str(e)))
            return None

    def _parse_list_field(self, column: str, raw: str, constructor) -> list:
        results = []
        for el in raw.split("|"):
            if not el.strip():
                continue
            try:
                results.append(constructor(el))
            except (ValueError, KeyError) as e:
                self._errors.append((column, el, raw, str(e)))
        return results


class HerrnhutPerson(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], PersonID)

        self.hidden = self._parse_field(
            "Übernahme in Personenlexikon",
            input_data["Übernahme in Personenlexikon"],
            partial(EncodedString, codelist={"ja": True, "nein": False}),
        )

        self.name = SimpleNamespace()
        self.name.preferred = self._parse_field(
            "Name - Vorzugsname", input_data["Name - Vorzugsname"], String
        )
        self.name.surname = self._parse_field(
            "Name - Nachname(n)", input_data["Name - Nachname(n)"], String
        )
        self.name.birth_name = self._parse_field(
            "Name - Geburtsname(n)", input_data["Name - Geburtsname(n)"], String
        )
        self.name.given_name = self._parse_field(
            "Name - Vorname(n)", input_data["Name - Vorname(n)"], String
        )
        self.name.title = self._parse_field(
            "Name - Titel", input_data["Name - Titel"], String
        )
        self.name.notes = self._parse_field(
            "Name - Anmerkungen", input_data["Name - Anmerkungen"], String
        )

        self.relatives = SimpleNamespace()
        self.relatives.siblings = self._parse_list_field(
            "Angehörige - Geschwister", input_data["Angehörige - Geschwister"], PersonID
        )
        self.relatives.spouses = self._parse_list_field(
            "Angehörige - Ehepartner", input_data["Angehörige - Ehepartner"], PersonID
        )
        self.relatives.children = self._parse_list_field(
            "Angehörige - Kinder", input_data["Angehörige - Kinder"], PersonID
        )
        self.relatives.notes = self._parse_field(
            "Angehörige - Anmerkungen", input_data["Angehörige - Anmerkungen"], String
        )

        self.links = SimpleNamespace()
        self.links.wikidata = self._parse_field(
            "Links - Wikidata", input_data["Links - Wikidata"], URL
        )
        self.links.gnd = self._parse_field(
            "Links - GND", input_data["Links - GND"], URL
        )
        self.links.factgrid = self._parse_field(
            "Links - FactGrid", input_data["Links - FactGrid"], URL
        )
        self.links.bionomia = self._parse_field(
            "Links - Bionomia", input_data["Links - Bionomia"], URL
        )
        self.links.saebi = self._parse_field(
            "Links - Säbi", input_data["Links - Säbi"], URL
        )

        self.member_of_moravians = self._parse_list_field(
            "Zugehörigkeit Herrnhuter Brüdergemeine",
            input_data["Zugehörigkeit Herrnhuter Brüdergemeine"],
            partial(
                EncodedString,
                codelist={
                    "ja-a": "qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen",
                    "ja-b": "als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte",
                    "ja-c": "Übernahme von kirchlichen Ämtern innerhalb der Brüdergemeine",
                    "ja-d": "Übernahme von Ämtern im Erziehungswesen der Brüdergemeine",
                    "nein-a": "ausgetreten",
                    "nein-b": "aber wichtig im Netzwerk",
                    "nein-c": "um Verwechslung auszuschließen",
                    "unbekannt": "Zugehörigkeit kann nicht ausgeschlossen werden.",
                },
            ),
        )

        self.birth = SimpleNamespace()
        self.birth.date = self._parse_field(
            "Geburt - Datum",
            input_data["Geburt - Datum"],
            lambda v: ISO8601_2_Date(v, require_source=True),
        )
        self.birth.date_notes = self._parse_field(
            "Geburt - Datum - Anmerkungen",
            input_data["Geburt - Datum - Anmerkungen"],
            String,
        )
        self.birth.location = self._parse_field(
            "Geburt - Ort",
            input_data["Geburt - Ort"],
            lambda v: LocationID(v, require_source=True),
        )
        self.birth.location_notes = self._parse_field(
            "Geburt - Ort - Anmerkungen",
            input_data["Geburt - Ort - Anmerkungen"],
            String,
        )

        self.death = SimpleNamespace()
        self.death.date = self._parse_field(
            "Tod - Datum",
            input_data["Tod - Datum"],
            lambda v: ISO8601_2_Date(v, require_source=True),
        )
        self.death.date_notes = self._parse_field(
            "Tod - Datum - Anmerkungen", input_data["Tod - Datum - Anmerkungen"], String
        )
        self.death.location = self._parse_field(
            "Tod - Ort",
            input_data["Tod - Ort"],
            lambda v: LocationID(v, require_source=True),
        )
        self.death.location_notes = self._parse_field(
            "Tod - Ort - Anmerkungen", input_data["Tod - Ort - Anmerkungen"], String
        )

        self.places_of_effect = self._parse_list_field(
            "Wirkungsorte", input_data["Wirkungsorte"], PlaceOfEffect
        )

        self.moravian_curriculum_vitae = self._parse_list_field(
            "Herrnhuter Lebenslauf", input_data["Herrnhuter Lebenslauf"], WorkID
        )

        self.contact = SimpleNamespace()
        self.contact.with_moravians = self._parse_list_field(
            "Kontakt - Mit Herrnhutern",
            input_data["Kontakt - Mit Herrnhutern"],
            lambda v: PersonID(v, require_source=True),
        )
        self.contact.with_non_moravians = self._parse_list_field(
            "Kontakt - Mit Nicht-Herrnhutern",
            input_data["Kontakt - Mit Nicht-Herrnhutern"],
            lambda v: PersonID(v, require_source=True),
        )

        self.botany = SimpleNamespace()
        self.botany.focuses = self._parse_list_field(
            "Botanik - Foki", input_data["Botanik - Foki"], String
        )

        self.botany.contribution_to_collections = SimpleNamespace()
        self.botany.contribution_to_collections.object_evidence = (
            self._parse_list_field(
                "Botanik - Beitrag zu Sammlungen (Objektnachweis)",
                input_data["Botanik - Beitrag zu Sammlungen (Objektnachweis)"],
                lambda v: CollectionID(v, require_source=True),
            )
        )
        self.botany.contribution_to_collections.database_evidence = (
            self._parse_list_field(
                "Botanik - Beitrag zu Sammlungen (Datenbanknachweis)",
                input_data["Botanik - Beitrag zu Sammlungen (Datenbanknachweis)"],
                lambda v: CollectionID(v, require_source=True),
            )
        )
        self.botany.contribution_to_collections.literature_evidence = (
            self._parse_list_field(
                "Botanik - Beitrag zu Sammlungen (Literaturnachweis)",
                input_data["Botanik - Beitrag zu Sammlungen (Literaturnachweis)"],
                lambda v: CollectionID(v, require_source=True),
            )
        )
        self.botany.contribution_to_collections.notes = self._parse_field(
            "Botanik - Beitrag zu Sammlungen - Anmerkungen",
            input_data["Botanik - Beitrag zu Sammlungen - Anmerkungen"],
            String,
        )

        self.botany.works = SimpleNamespace()
        self.botany.works.manuscripts = self._parse_list_field(
            "Botanik - Manuskripte der Person",
            input_data["Botanik - Manuskripte der Person"],
            ManuscriptID,
        )
        self.botany.works.printed = self._parse_list_field(
            "Botanik - Druckwerke der Person",
            input_data["Botanik - Druckwerke der Person"],
            LiteratureID,
        )

        self.botany.citations = SimpleNamespace()
        self.botany.citations.in_botanical_works_by_others = self._parse_list_field(
            "Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere",
            input_data[
                "Botanik - Erwähnungen der Person in Werken mit botanischen Kontext durch Andere"
            ],
            WorkID,
        )

        self.works = SimpleNamespace()
        self.works.without_botanical_context = self._parse_list_field(
            "Wichtige Werke der Person ohne botanischen Kontext",
            input_data["Wichtige Werke der Person ohne botanischen Kontext"],
            WorkID,
        )

        self.citations = SimpleNamespace()
        self.citations.in_non_botanical_works_by_others = self._parse_list_field(
            "Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere",
            input_data[
                "Erwähnungen der Person in Werken ohne botanischen Kontext durch Andere"
            ],
            WorkID,
        )

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        """Enrich person links (gnd, factgrid, bionomia, saebi) from Wikidata.
        Only fills fields that are currently empty; never overwrites.
        """
        wikidata_url = getattr(self.links.wikidata, "url", None)
        if not wikidata_url:
            return
        try:
            data = fetch_person_data_from_wikipedia(
                wikidata_url, cache_path, rewrite_cache=rewrite_cache
            )
        except Exception as e:
            warnings.warn(
                f"Wikidata enrichment failed for person {self.id} ({wikidata_url}): {e}"
            )
            return

        if data["gnd"] and not self.links.gnd:
            self.links.gnd = self._parse_field("Links - GND", data["gnd"], URL)
        if data["factgrid"] and not self.links.factgrid:
            self.links.factgrid = self._parse_field(
                "Links - FactGrid", data["factgrid"], URL
            )
        if data["bionomia"] and not self.links.bionomia:
            self.links.bionomia = self._parse_field(
                "Links - Bionomia", data["bionomia"], URL
            )
        if data["saebi"] and not self.links.saebi:
            self.links.saebi = self._parse_field("Links - Säbi", data["saebi"], URL)

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutArchive(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], ArchiveID)
        self.name = self._parse_field("Name", input_data["Name"], String)
        self.abbreviations = self._parse_list_field(
            "Abkürzungen", input_data["Abkürzungen"], String
        )
        self.link = self._parse_field("Link", input_data["Link"], URL)

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutManuscript(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], ManuscriptID)
        self.archive = self._parse_field("Archiv", input_data["Archiv"], ArchiveID)
        self.signature = self._parse_field("Signatur", input_data["Signatur"], String)
        self.title = self._parse_field("Titel", input_data["Titel"], String)
        self.permalink = self._parse_field("Permalink", input_data["Permalink"], URL)
        self.description = self._parse_field(
            "Beschreibung", input_data["Beschreibung"], String
        )
        self.wikidata_id = self._parse_field(
            "Wikidata ID", input_data["Wikidata ID"], String
        )

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutLiterature(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], LiteratureID)
        self.title = self._parse_field("Titel", input_data["Titel"], String)
        self.permalink = self._parse_field("Permalink", input_data["Permalink"], URL)
        self.description = self._parse_field(
            "Beschreibung", input_data["Beschreibung"], String
        )

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutLocation(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], LocationID)
        self.name = self._parse_field("Name", input_data["Name"], String)
        self.variants = self._parse_list_field(
            "Varianten", input_data["Varianten"], Variant
        )
        self.wikidata = self._parse_field("Wikidata", input_data["Wikidata"], URL)
        self.description = self._parse_field(
            "Beschreibung", input_data["Beschreibung"], String
        )

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        """Enrich location with coordinates, temporal range, and founder from Wikidata.
        Adds attributes: coordinates ({lat, lon} or None), start, end, founder.
        """
        wikidata_url = getattr(self.wikidata, "url", None)
        if not wikidata_url:
            return
        try:
            data = fetch_location_data_from_wikidata(
                wikidata_url, cache_path, rewrite_cache=rewrite_cache
            )
        except Exception as e:
            warnings.warn(
                f"Wikidata enrichment failed for location {self.id} ({wikidata_url}): {e}"
            )
            return
        self.coordinates = data["coordinates"]  # {lat, lon} or None
        self.start = data["start"]  # ISO datetime string or None
        self.end = data["end"]  # ISO datetime string or None
        self.founder = data["founder"]  # label string or None

    def serialize_json(self):
        raise NotImplementedError


class HerrnhutCollection(HerrnhutObject):
    def _parse_input(self, input_data: dict):
        self.id = self._parse_field("ID", input_data["ID"], CollectionID)
        self.nybg_herbarium_code = self._parse_field(
            "NYBG Herbarcode", input_data["NYBG Herbarcode"], String
        )
        self.name = self._parse_field(
            "Name der Sammlung", input_data["Name der Sammlung"], String
        )
        self.part_of_collection = self._parse_field(
            "Teilsammlung von", input_data["Teilsammlung von"], CollectionID
        )
        self.holding_institutions = self._parse_list_field(
            "Sammlungshaltende Institution",
            input_data["Sammlungshaltende Institution"],
            String,
        )
        self.website = self._parse_field("Webseite", input_data["Webseite"], URL)
        self.notes = self._parse_field("Anmerkungen", input_data["Anmerkungen"], String)

    def enrich(self, cache_path: str, rewrite_cache: bool = False):
        raise NotImplementedError

    def serialize_json(self):
        raise NotImplementedError
