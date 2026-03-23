window.AppModel = (() => {
  const PERSONS_URL = "./data/persons.json";
  const LOCATIONS_URL = "./data/locations.json";

  const state = {
    personsById: {},
    filteredPersonIds: [],
    locationsById: {},
    selectedPersonId: null,
    map: null,
    mapLayers: [],
  };

  const MARKER_COLORS = {
    birth: "#198754",
    death: "#dc3545",
    activity: "#0d6efd",
  };

  const LINK_ICONS = {
    wikidata: {
      src: "./assets/wikidata_18x12.svg",
      alt: "Wikidata",
      text: "Wikidata",
    },
    gnd: {
      src: "./assets/gnd.png",
      alt: "GND",
      text: "GND",
    },
    factgrid: {
      src: "./assets/factgrid.png",
      alt: "FactGrid",
      text: "FactGrid",
    },
    bionomia: {
      src: "./assets/bionomia.png",
      alt: "Bionomia",
      text: "Bionomia",
    },
    saebi: {
      src: "./assets/saebi.png",
      alt: "Säbi",
      text: "Säbi",
    },
  };

  async function loadData() {
    const [personsResponse, locationsResponse] = await Promise.all([
      fetch(PERSONS_URL),
      fetch(LOCATIONS_URL),
    ]);
    const personsPayload = await personsResponse.json();
    const locationsPayload = await locationsResponse.json();

    state.personsById = personsPayload;
    state.filteredPersonIds = Object.keys(personsPayload).sort((a, b) => {
      const leftSurname = personsPayload[a].name.surname.value.value;
      const rightSurname = personsPayload[b].name.surname.value.value;
      return leftSurname.localeCompare(rightSurname, "de");
    });
    state.locationsById = locationsPayload;
    state.selectedPersonId = state.filteredPersonIds[0];
  }

  function formatTypedValue(typedValue) {
    if (typedValue.type === "List") {
      return typedValue.value.map((entry) => entry.value).join(", ");
    }

    return typedValue.value;
  }

  function formatLifeEvent(eventObject) {
    const dates = eventObject.date.value.value.map((entry) => entry.value);
    const locations = eventObject.location.value.value.map((entry) => entry.value);
    const dateText = Array.isArray(dates) ? dates.join(", ") : dates;
    const locationText = Array.isArray(locations) ? locations.join(", ") : locations;

    return [dateText, locationText].filter(Boolean).join(" | ");
  }

  function countListEntries(field) {
    return field.value.value.length;
  }

  function getLifeEventLabel(eventObject) {
    return eventObject.date.label.split(" - ")[0];
  }

  function collectPersonPlaces(record) {
    const places = [];

    addLifeLocations(places, record.life.birth.location, "birth", "Geburtsort");
    addLifeLocations(places, record.life.death.location, "death", "Todesort");

    const activities = record.life.places_of_effect.value.value;

    activities.forEach((entry) => {
      const values = entry.value.values;
      const temporal = values[0].value;
      const locationId = values[1].value;
      const institution = values[2].value;
      const role = values[3].value;

      const locationRecord = state.locationsById[locationId];
      if (!locationRecord || !("longitude" in locationRecord) || !("latitude" in locationRecord)) {
        return;
      }
      const longitude = locationRecord.longitude.value.value;
      const latitude = locationRecord.latitude.value.value;

      const parts = [temporal, institution, role].filter(Boolean);
      places.push({
        type: "activity",
        title: locationRecord.name.value.value,
        subtitle: parts.join(" | "),
        latitude,
        longitude,
      });
    });

    return deduplicatePlaces(places);
  }

  function addLifeLocations(target, field, type, label) {
    const values = field.value.value;

    values.forEach((entry) => {
      const locationRecord = state.locationsById[entry.value];
      if (!locationRecord || !("longitude" in locationRecord) || !("latitude" in locationRecord)) {
        return;
      }
      const longitude = locationRecord.longitude.value.value;
      const latitude = locationRecord.latitude.value.value;

      target.push({
        type,
        title: locationRecord.name.value.value,
        subtitle: label,
        latitude,
        longitude,
      });
    });
  }

  function deduplicatePlaces(places) {
    const seen = new Set();

    return places.filter((place) => {
      const key = [
        place.type,
        place.title,
        place.latitude,
        place.longitude,
        place.subtitle,
      ].join("|");

      if (seen.has(key)) {
        return false;
      }

      seen.add(key);
      return true;
    });
  }

  return {
    PERSONS_URL,
    LOCATIONS_URL,
    state,
    MARKER_COLORS,
    LINK_ICONS,
    loadData,
    formatTypedValue,
    formatLifeEvent,
    countListEntries,
    getLifeEventLabel,
    collectPersonPlaces,
  };
})();
