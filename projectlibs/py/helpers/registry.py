"""Registry for cross-referencing HerrnhutObject instances by ID.

Pass a Registry instance to to_dict() calls so that ID references can
be resolved to human-readable labels and links.
"""

from __future__ import annotations

from projectlibs.py.field_datatypes import LiteratureID


class Registry:
    """Holds all top-level object collections and resolves cross-references.

    Each resolve_* method accepts an ID object (with a .id attribute) or a
    plain ID string and returns a dict with "id", "label", and "link" keys,
    or None if the input is absent.
    """

    def __init__(
        self,
        persons=None,
        locations=None,
        archives=None,
        manuscripts=None,
        literature=None,
        collections=None,
    ):
        self._persons = self._index(persons)
        self._locations = self._index(locations)
        self._archives = self._index(archives)
        self._manuscripts = self._index(manuscripts)
        self._literature = self._index(literature)
        self._collections = self._index(collections)

    @staticmethod
    def _index(d: dict | None) -> dict:
        if not d:
            return {}
        result = {}
        for obj in d.values():
            key = getattr(getattr(obj, "id", None), "id", None)
            if key:
                result[key] = obj
        return result

    @staticmethod
    def _id_str(id_obj_or_str) -> str | None:
        if id_obj_or_str is None:
            return None
        if isinstance(id_obj_or_str, str):
            return id_obj_or_str or None
        return getattr(id_obj_or_str, "id", None)

    @staticmethod
    def _ref(raw_id: str, label, link) -> dict:
        return {"id": raw_id, "label": label if label else raw_id, "link": link}

    def resolve_person(self, id_obj) -> dict | None:
        raw = self._id_str(id_obj)
        if not raw:
            return None
        obj = self._persons.get(raw)
        label = (
            getattr(
                getattr(getattr(obj, "name", None), "preferred", None), "value", None
            )
            if obj
            else None
        )
        link = (
            getattr(getattr(getattr(obj, "links", None), "wikidata", None), "url", None)
            if obj
            else None
        )
        return self._ref(raw, label, link)

    def resolve_location(self, id_obj_or_str) -> dict | None:
        raw = (
            self._id_str(id_obj_or_str)
            if not isinstance(id_obj_or_str, str)
            else (id_obj_or_str or None)
        )
        if not raw:
            return None
        obj = self._locations.get(raw)
        label = getattr(getattr(obj, "name", None), "value", None) if obj else None
        link = getattr(getattr(obj, "wikidata", None), "url", None) if obj else None
        return self._ref(raw, label, link)

    def resolve_archive(self, id_obj) -> dict | None:
        raw = self._id_str(id_obj)
        if not raw:
            return None
        obj = self._archives.get(raw)
        label = getattr(getattr(obj, "name", None), "value", None) if obj else None
        link = getattr(getattr(obj, "link", None), "url", None) if obj else None
        return self._ref(raw, label, link)

    def resolve_manuscript(self, id_obj) -> dict | None:
        raw = self._id_str(id_obj)
        if not raw:
            return None
        obj = self._manuscripts.get(raw)
        label = getattr(getattr(obj, "title", None), "value", None) if obj else None
        link = getattr(getattr(obj, "permalink", None), "url", None) if obj else None
        return self._ref(raw, label, link)

    def resolve_literature(self, id_obj) -> dict | None:
        raw = self._id_str(id_obj)
        if not raw:
            return None
        obj = self._literature.get(raw)
        label = getattr(getattr(obj, "title", None), "value", None) if obj else None
        link = getattr(getattr(obj, "permalink", None), "url", None) if obj else None
        return self._ref(raw, label, link)

    def resolve_collection(self, id_obj) -> dict | None:
        raw = self._id_str(id_obj)
        if not raw:
            return None
        obj = self._collections.get(raw)
        label = getattr(getattr(obj, "name", None), "value", None) if obj else None
        link = getattr(getattr(obj, "website", None), "url", None) if obj else None
        return self._ref(raw, label, link)

    def resolve_work(self, work_id_obj) -> dict | None:
        """WorkID wraps a LiteratureID or ManuscriptID in .document."""
        if work_id_obj is None:
            return None
        inner = getattr(work_id_obj, "document", None)
        if inner is None:
            return None
        if isinstance(inner, LiteratureID):
            return self.resolve_literature(inner)
        return self.resolve_manuscript(inner)
