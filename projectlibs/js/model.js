window.AppModel = (() => {
  const PERSONS_URL = "./data/geopersons.json";
  const LOCATIONS_URL = "./data/locations.json";

  const state = {
    personsById: {},
    filteredPersonIds: [],
    locationsById: {},
    selectedPersonId: null,
    map: null,
    mapSource: null,
    mapOverlay: null,
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
    state.selectedPersonId = null;
  }

  function formatTypedValue(typedValue) {
    if (typedValue.type === "List") {
      return typedValue.value
        .map((entry) => (typeof entry === "object" ? entry.value : entry))
        .join(", ");
    }

    return typedValue.value;
  }

  function formatFeatureTime(timeObject) {
    if ("date" in timeObject) {
      return timeObject.date;
    }

    if ("timestamp" in timeObject) {
      return timeObject.timestamp;
    }

    if ("interval" in timeObject) {
      return timeObject.interval.join(" / ");
    }

    return "";
  }

  function ationNameForFeature(feature) {
    const [featureLongitude, featureLatitude] = feature.geometry.coordinates;

    for (const location of Object.values(state.locationsById)) {
      if (!("longitude" in location) || !("latitude" in location)) {
        continue;
      }

      const locationLongitude = location.longitude.value.value;
      const locationLatitude = location.latitude.value.value;

      if (locationLongitude === featureLongitude && locationLatitude === featureLatitude) {
        return location.name.value.value;
      }
    }

    return "";
  }


  function collectPersonPlaces(record) {
    return deduplicatePlaces(
      record.life_trajectory.features.map((feature) => {
        const [longitude, latitude] = feature.geometry.coordinates;

        return {
          type: feature.featureType === "place_of_effect" ? "activity" : feature.featureType,
          title: feature.featureType,
          subtitle: [
            formatFeatureTime(feature.time),
            feature.properties.institution,
            feature.properties.occupation,
          ]
            .filter(Boolean)
            .join(" | "),
          latitude,
          longitude,
        };
      })
    );
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
    formatFeatureTime,
    collectPersonPlaces,
  };
})();
