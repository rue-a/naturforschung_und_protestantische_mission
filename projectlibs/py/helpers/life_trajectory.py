"""JSON-FG life trajectory builder for HerrnhutPerson objects.

JSON-FG spec: https://docs.ogc.org/DRAFTS/21-045.html
Each Feature carries:
  - "type": "Feature"
  - "featureType": one of "birth" | "death" | "place_of_effect"
  - "time": JSON-FG time object (date, interval)
  - "geometry": GeoJSON Point [lon, lat] or null
  - "properties": location metadata + event-specific fields

The `time` values use ISO 8601-2 EDTF notation as stored on field objects
(e.g. "1738~", "1782/1785", "/1800").
"""

from __future__ import annotations

JSON_FG_CONFORMS_TO = "http://www.opengis.net/spec/json-fg-1/0.2/conf/core"


# ── helpers ───────────────────────────────────────────────────────────────────


def _build_time(temporal_str: str | None) -> dict | None:
    """Convert an ISO 8601-2 date or period string to a JSON-FG time object.

    Examples:
      "1738~"        → {"date": "1738~"}
      "1782/1785"    → {"interval": ["1782", "1785"]}
      "/1800"        → {"interval": ["..", "1800"]}
      "1782/"        → {"interval": ["1782", ".."]}
    """
    if not temporal_str:
        return None
    temporal_str = temporal_str.strip()
    if not temporal_str:
        return None
    if "/" in temporal_str:
        start, end = temporal_str.split("/", 1)
        return {"interval": [start.strip() or "..", end.strip() or ".."]}
    return {"date": temporal_str}


def _build_geometry(location) -> dict | None:
    """Build a GeoJSON Point from a HerrnhutLocation object.

    Returns None if the location is missing or has no coordinates (e.g.
    Wikidata enrichment was skipped or the location has no Wikidata entry).
    """
    if location is None:
        return None
    coords = getattr(location, "coordinates", None)
    if not coords:
        return None
    return {"type": "Point", "coordinates": [coords["lon"], coords["lat"]]}


def _location_properties(location) -> dict:
    """Return a minimal properties dict describing the location."""
    if location is None:
        return {"location_wikidata": None, "place_name": None}
    lwikidata = getattr(getattr(location, "wikidata", None), "url", None)
    lname = getattr(getattr(location, "name", None), "value", None)
    return {"location_wikidata": lwikidata, "place_name": lname}


# ── public classes ────────────────────────────────────────────────────────────


class LifeTrajectoryFeature:
    """One JSON-FG Feature in a person's life trajectory."""

    def __init__(
        self,
        *,
        feature_type: str,
        time: dict | None,
        geometry: dict | None,
        properties: dict,
    ):
        self.feature_type = feature_type
        self.time = time
        self.geometry = geometry
        self.properties = properties

    def to_dict(self) -> dict:
        return {
            "type": "Feature",
            "featureType": self.feature_type,
            "time": self.time,
            "geometry": self.geometry,
            "properties": self.properties,
        }


class LifeTrajectory:
    """JSON-FG FeatureCollection representing a person's life trajectory.

    Parameters
    ----------
    person:
        A ``HerrnhutPerson`` instance (after parsing and optional enrichment).
    locations:
        The locations dict as returned by ``load_objects``, i.e. keyed by
        ``LocationID`` objects.  Normalised to string keys internally.
    """

    def __init__(self, person, locations: dict):
        # Normalise to string-keyed lookup so we can look up by bare ID string
        # (as stored on PlaceOfEffect.place) or LocationID.id attribute.
        self._locs: dict = {
            loc.id.id: loc
            for loc in locations.values()
            if getattr(getattr(loc, "id", None), "id", None)
        }
        self.features: list[LifeTrajectoryFeature] = []
        self._build(person)

    # ── private ───────────────────────────────────────────────────────────────

    def _resolve(self, location_id_obj) -> object | None:
        """Resolve a LocationID object to a HerrnhutLocation, or None."""
        if location_id_obj is None:
            return None
        lid = getattr(location_id_obj, "id", None)
        if lid is None:
            return None
        return self._locs.get(lid)

    def _build(self, person) -> None:
        # birth
        birth_date = getattr(person.birth, "date", None)
        if birth_date is not None:
            loc = self._resolve(getattr(person.birth, "location", None))
            props = _location_properties(loc)
            self.features.append(
                LifeTrajectoryFeature(
                    feature_type="birth",
                    time=_build_time(getattr(birth_date, "date", None)),
                    geometry=_build_geometry(loc),
                    properties=props,
                )
            )

        # death
        death_date = getattr(person.death, "date", None)
        if death_date is not None:
            loc = self._resolve(getattr(person.death, "location", None))
            props = _location_properties(loc)
            self.features.append(
                LifeTrajectoryFeature(
                    feature_type="death",
                    time=_build_time(getattr(death_date, "date", None)),
                    geometry=_build_geometry(loc),
                    properties=props,
                )
            )

        # places of effect
        for poe in person.places_of_effect or []:
            temporal_str = getattr(getattr(poe, "temporal", None), "raw", "").strip()
            loc_id_str = getattr(getattr(poe, "place", None), "id", "")
            loc = self._locs.get(loc_id_str)
            props = _location_properties(loc)
            props["institution"] = getattr(poe, "institution", "").strip() or None
            props["occupation"] = getattr(poe, "occupation", "").strip() or None
            self.features.append(
                LifeTrajectoryFeature(
                    feature_type="place_of_effect",
                    time=_build_time(temporal_str),
                    geometry=_build_geometry(loc),
                    properties=props,
                )
            )

    # ── public ────────────────────────────────────────────────────────────────

    def to_dict(self) -> dict:
        return {
            "type": "FeatureCollection",
            "conformsTo": [JSON_FG_CONFORMS_TO],
            "features": [f.to_dict() for f in self.features],
        }
