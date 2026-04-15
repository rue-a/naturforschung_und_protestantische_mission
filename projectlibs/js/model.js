window.AppModel = (() => {
  const PERSONS_URL = "./data/geopersons.json";
  const LOCATIONS_URL = "./data/locations.json";

  const state = {
    personsById: {},
    filteredPersonIds: [],
    locationsById: {},
    selectedPersonId: null,
    appBasePath: "/",
    map: null,
    mapSource: null,
    mapOverlay: null,
    mapTimeYear: null,
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

  function unwrapTypedValue(value) {
    if (Array.isArray(value)) {
      return value.map(unwrapTypedValue);
    }

    if (!value || typeof value !== "object") {
      return value;
    }

    if ("type" in value && "value" in value) {
      if (value.type === "List" && Array.isArray(value.value)) {
        return value.value.map(unwrapTypedValue);
      }

      return unwrapTypedValue(value.value);
    }

    return value;
  }

  function getFieldValue(field) {
    if (!field || typeof field !== "object" || !("value" in field)) {
      return "";
    }

    const value = unwrapTypedValue(field.value);
    return value ?? "";
  }

  function getPersonSortName(record) {
    return String(
      getFieldValue(record.name.surname) || getFieldValue(record.name.preferred) || ""
    );
  }

  function getPathSegments(pathname = window.location.pathname) {
    return pathname.split("/").filter(Boolean);
  }

  function getRoutePersonId(pathname = window.location.pathname) {
    const segments = getPathSegments(pathname);
    const lastSegment = segments.at(-1);
    if (!lastSegment || lastSegment === "index.html") {
      return null;
    }

    const personId = decodeURIComponent(lastSegment);
    return personId in state.personsById ? personId : null;
  }

  function getAppBasePath(pathname = window.location.pathname) {
    const segments = getPathSegments(pathname);

    if (segments.length > 0) {
      const lastSegment = decodeURIComponent(segments.at(-1));
      if (lastSegment in state.personsById) {
        segments.pop();
      }
    }

    if (segments.at(-1) === "index.html") {
      segments.pop();
    }

    if (segments.length === 0) {
      return "/";
    }

    return `/${segments.join("/")}`;
  }

  function buildPersonPath(personId) {
    const encodedPersonId = encodeURIComponent(personId);
    const basePath = state.appBasePath === "/" ? "" : state.appBasePath;
    return `${basePath}/${encodedPersonId}`;
  }

  function updateSelectedPersonUrl(personId, { replace = false } = {}) {
    const nextPath = buildPersonPath(personId);
    const currentPath = window.location.pathname.replace(/\/+$/, "") || "/";

    if (currentPath === nextPath) {
      return;
    }

    const method = replace ? "replaceState" : "pushState";
    window.history[method]({ personId }, "", nextPath);
  }

  async function loadData() {
    const [personsResponse, locationsResponse] = await Promise.all([
      fetch(PERSONS_URL),
      fetch(LOCATIONS_URL),
    ]);
    const personsPayload = await personsResponse.json();
    const locationsPayload = await locationsResponse.json();

    state.personsById = personsPayload;
    state.filteredPersonIds = Object.keys(personsPayload).sort((a, b) => {
      return getPersonSortName(personsPayload[a]).localeCompare(
        getPersonSortName(personsPayload[b]),
        "de"
      );
    });
    state.locationsById = locationsPayload;
    state.selectedPersonId = null;
    state.appBasePath = getAppBasePath();
  }

  function formatTypedValue(typedValue) {
    const value = unwrapTypedValue(typedValue);

    if (Array.isArray(value)) {
      return value.join(", ");
    }

    return value ?? "";
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

  function getLocationNameForFeature(feature) {
    const [featureLongitude, featureLatitude] = feature.geometry.coordinates;

    for (const location of Object.values(state.locationsById)) {
      if (!("longitude" in location) || !("latitude" in location)) {
        continue;
      }

      const locationLongitude = getFieldValue(location.longitude);
      const locationLatitude = getFieldValue(location.latitude);

      if (locationLongitude === featureLongitude && locationLatitude === featureLatitude) {
        return getFieldValue(location.name);
      }
    }

    return "";
  }


  function collectPersonPlaces(record) {
    return deduplicatePlaces(
      record.life_trajectory.features.map((feature) => {
        const [longitude, latitude] = feature.geometry.coordinates;
        const timeRange = getFeatureYearRange(feature.time);

        return {
          type: feature.featureType === "place_of_effect" ? "activity" : feature.featureType,
          title: getLocationNameForFeature(feature) || feature.featureType,
          subtitle: [
            formatFeatureTime(feature.time),
            feature.properties.institution,
            feature.properties.occupation,
          ]
            .filter(Boolean)
            .join(" | "),
          latitude,
          longitude,
          startYear: timeRange.startYear,
          endYear: timeRange.endYear,
        };
      })
    );
  }

  function getFeatureYearRange(timeObject) {
    if ("date" in timeObject) {
      const year = extractYear(timeObject.date);
      return { startYear: year, endYear: year };
    }

    if ("timestamp" in timeObject) {
      const year = extractYear(timeObject.timestamp);
      return { startYear: year, endYear: year };
    }

    if ("interval" in timeObject) {
      return {
        startYear: extractYear(timeObject.interval[0]),
        endYear: extractYear(timeObject.interval[1]),
      };
    }

    return { startYear: null, endYear: null };
  }

  function extractYear(value) {
    if (!value || value === "..") {
      return null;
    }

    const match = String(value).match(/^-?\d+/);
    if (!match) {
      return null;
    }

    return Number(match[0]);
  }

  function getPlacesYearExtent(places) {
    const years = places.flatMap((place) => [place.startYear, place.endYear]).filter(
      (year) => Number.isFinite(year)
    );

    if (years.length === 0) {
      return null;
    }

    return {
      minYear: Math.min(...years),
      maxYear: Math.max(...years),
    };
  }

  function filterPlacesByYear(places, year) {
    if (!Number.isFinite(year)) {
      return places;
    }

    return places.filter((place) => {
      if (place.startYear === null && place.endYear === null) {
        return true;
      }

      const lowerBound = place.startYear === null ? -Infinity : place.startYear;
      const upperBound = place.endYear === null ? Infinity : place.endYear;

      return lowerBound <= year && year <= upperBound;
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
    getFieldValue,
    getPersonSortName,
    getRoutePersonId,
    updateSelectedPersonUrl,
    formatTypedValue,
    formatFeatureTime,
    getPlacesYearExtent,
    filterPlacesByYear,
    collectPersonPlaces,
  };
})();
