"""Compute an importance measure for each location based on person events.

For every HerrnhutPerson, three event types are tracked per location:
  - births:           person was born there  → {id, name, date}
  - deaths:           person died there      → {id, name, date}
  - places_of_effect: person had a POE there → {id, name, temporal, institution, occupation}

Only locations referenced by a proper L-ID are included; free-text place
strings in places_of_effect that don't match the ID pattern are ignored.
Each person appears at most once per birth/death category; POE entries are
kept individually so that multiple roles at the same place are preserved,
but duplicate (person, temporal, institution, occupation) tuples are dropped.
"""

from __future__ import annotations

import re
from collections import defaultdict

_LOC_ID_RE = re.compile(r"^L\d{7}$")


def _base_ref(person) -> dict:
    return {
        "id": getattr(getattr(person, "id", None), "id", None),
        "name": getattr(getattr(person.name, "preferred", None), "value", None),
    }


def compute_location_importance(persons: dict) -> dict[str, dict]:
    """Return per-location person lists derived from all persons."""
    result: dict[str, dict] = defaultdict(
        lambda: {"births": [], "deaths": [], "places_of_effect": []}
    )
    seen_births: dict[str, set] = defaultdict(set)
    seen_deaths: dict[str, set] = defaultdict(set)
    seen_poe: dict[str, set] = defaultdict(set)

    for person in persons.values():
        base = _base_ref(person)
        pid = base["id"]

        birth_id = getattr(
            getattr(getattr(person, "birth", None), "location", None), "id", None
        )
        if birth_id and pid not in seen_births[birth_id]:
            date_obj = getattr(getattr(person, "birth", None), "date", None)
            result[birth_id]["births"].append(
                {
                    **base,
                    "date": date_obj.formatted() if date_obj else None,
                }
            )
            seen_births[birth_id].add(pid)

        death_id = getattr(
            getattr(getattr(person, "death", None), "location", None), "id", None
        )
        if death_id and pid not in seen_deaths[death_id]:
            date_obj = getattr(getattr(person, "death", None), "date", None)
            result[death_id]["deaths"].append(
                {
                    **base,
                    "date": date_obj.formatted() if date_obj else None,
                }
            )
            seen_deaths[death_id].add(pid)

        for poe in getattr(person, "places_of_effect", []):
            place = (getattr(poe, "place", "") or "").strip()
            if not _LOC_ID_RE.match(place):
                continue
            temporal = poe.formatted_temporal()
            institution = (getattr(poe, "institution", "") or "").strip() or None
            occupation = (getattr(poe, "occupation", "") or "").strip() or None
            key = (pid, temporal, institution, occupation)
            if key not in seen_poe[place]:
                result[place]["places_of_effect"].append(
                    {
                        **base,
                        "temporal": temporal,
                        "institution": institution,
                        "occupation": occupation,
                    }
                )
                seen_poe[place].add(key)

    return dict(result)
