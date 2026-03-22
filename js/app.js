const PERSONS_URL = "./data/persons.json";
const LOCATIONS_URL = "./data/locations.json";

const state = {
  persons: [],
  filteredPersons: [],
  locationsById: new Map(),
  selectedPersonId: null,
  map: null,
  mapLayers: [],
};

const DOM = {
  loading: document.getElementById("loading-state"),
  error: document.getElementById("error-state"),
  appShell: document.getElementById("app-shell"),
  searchInput: document.getElementById("person-search"),
  browser: document.getElementById("person-browser"),
  metadata: document.getElementById("person-metadata"),
  article: document.getElementById("person-article"),
  links: document.getElementById("person-links"),
  mapSummary: document.getElementById("map-summary"),
  mapContainer: document.getElementById("person-map"),
  mapEmptyState: document.getElementById("map-empty-state"),
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

document.addEventListener("DOMContentLoaded", () => {
  initializeApp();
});

async function initializeApp() {
  try {
    const [personsPayload, locationsPayload] = await Promise.all([
      fetchJson(PERSONS_URL),
      fetchJson(LOCATIONS_URL),
    ]);

    state.persons = buildPersonIndex(personsPayload);
    state.filteredPersons = [...state.persons];
    state.locationsById = buildLocationIndex(locationsPayload);
    state.selectedPersonId = state.persons[0]?.id ?? null;

    setupMap();
    bindEvents();
    renderBrowser();
    renderSelectedPerson();

    DOM.loading.classList.add("d-none");
    DOM.appShell.classList.remove("d-none");
  } catch (error) {
    showError(error);
  }
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Konnte ${url} nicht laden (${response.status}).`);
  }
  return response.json();
}

function buildPersonIndex(payload) {
  return Object.entries(payload)
    .map(([id, record]) => ({
      id,
      record,
      name: getPreferredName(record) || id,
    }))
    .sort((a, b) => a.name.localeCompare(b.name, "de"));
}

function buildLocationIndex(payload) {
  const map = new Map();

  Object.entries(payload).forEach(([id, record]) => {
    const longitude = getTypedValue(record.longitude);
    const latitude = getTypedValue(record.latitude);

    map.set(id, {
      id,
      name: getTypedValue(record.name) || id,
      longitude: typeof longitude === "number" ? longitude : null,
      latitude: typeof latitude === "number" ? latitude : null,
      record,
    });
  });

  return map;
}

function bindEvents() {
  DOM.searchInput.addEventListener("input", handleSearch);
}

function handleSearch(event) {
  const query = event.target.value.trim().toLowerCase();

  state.filteredPersons = state.persons.filter((person) => {
    const haystack = [
      person.id,
      person.name,
      getTypedValue(person.record.name?.surname),
      getTypedValue(person.record.name?.given_name),
    ]
      .filter(Boolean)
      .join(" ")
      .toLowerCase();

    return haystack.includes(query);
  });

  if (!state.filteredPersons.some((person) => person.id === state.selectedPersonId)) {
    state.selectedPersonId = state.filteredPersons[0]?.id ?? null;
  }

  renderBrowser();
  renderSelectedPerson();
}

function renderBrowser() {
  DOM.browser.innerHTML = "";

  if (!state.filteredPersons.length) {
    DOM.browser.innerHTML =
      '<div class="list-group-item text-body-secondary">Keine Person gefunden.</div>';
    return;
  }

  state.filteredPersons.forEach((person) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className =
      "list-group-item list-group-item-action d-flex justify-content-between align-items-start";

    if (person.id === state.selectedPersonId) {
      button.classList.add("active");
    }

    button.innerHTML = `
      <div>
        <div class="fw-semibold">${escapeHtml(person.name)}</div>
        <div class="small ${person.id === state.selectedPersonId ? "text-white-50" : "text-body-secondary"}">${escapeHtml(person.id)}</div>
      </div>
    `;

    button.addEventListener("click", () => {
      state.selectedPersonId = person.id;
      renderBrowser();
      renderSelectedPerson();
    });

    DOM.browser.appendChild(button);
  });
}

function renderSelectedPerson() {
  const selectedPerson = state.filteredPersons.find(
    (person) => person.id === state.selectedPersonId
  );

  if (!selectedPerson) {
    DOM.metadata.innerHTML = "";
    DOM.article.innerHTML = "";
    DOM.links.innerHTML = "";
    renderMap([]);
    DOM.mapSummary.textContent = "Keine Person ausgewählt.";
    return;
  }

  renderMetadata(selectedPerson);
  renderArticle(selectedPerson);
  renderLinks(selectedPerson);
  renderMapForPerson(selectedPerson);
}

function renderMetadata(person) {
  const record = person.record;
  const metadataItems = [
    ["Bevorzugter Name", person.name],
    ["ID", person.id],
    ["Nachname", getTypedValue(record.name?.surname)],
    ["Vorname", getTypedValue(record.name?.given_name)],
    ["Mitgliedschaft", formatTypedValue(record.member_of_moravians?.value)],
    ["Geburt", formatLifeEvent(record.life?.birth)],
    ["Tod", formatLifeEvent(record.life?.death)],
  ].filter(([, value]) => value);

  DOM.metadata.innerHTML = metadataItems
    .map(
      ([label, value]) => `
        <div class="metadata-item compact">
          <span class="metadata-label">${escapeHtml(label)}</span>
          <p class="metadata-value mb-0">${escapeHtml(value)}</p>
        </div>
      `
    )
    .join("");
}

function renderArticle(person) {
  const record = person.record;
  const focusText = formatTypedValue(record.botany?.focuses?.value) || "noch nicht erfasst";
  const activityCount = countListEntries(record.life?.places_of_effect?.value);

  DOM.article.innerHTML = `
    <h2 class="h3 mb-0">${escapeHtml(person.name)}</h2>
    <p class="lead mb-0">
      Diese Spalte ist als Platzhalter fuer einen spaeteren biografischen Artikel gedacht.
      Schon jetzt kann sie genutzt werden, um eine automatisch erzeugte Kurzansicht zu zeigen.
    </p>
    <div class="article-placeholder">
      <p class="mb-2">
        <strong>${escapeHtml(person.name)}</strong> ist im aktuellen Datensatz als eigenstaendige Person erfasst.
        Die strukturierte Ansicht links und rechts kann bereits fuer Recherche, Verknuepfungen und kuratorische Arbeit genutzt werden.
      </p>
      <p class="mb-2">
        Botanische Foki: ${escapeHtml(focusText)}.
      </p>
      <p class="mb-0">
        Erfasste Wirkungsorte: ${escapeHtml(String(activityCount))}. Sobald Artikeltexte vorliegen,
        kann dieser Bereich problemlos durch HTML- oder Markdown-Inhalte ersetzt werden.
      </p>
    </div>
    <div>
      <h3 class="h6 text-body-secondary">Aktueller Stand</h3>
      <p class="mb-0">
        Der Personenbrowser verwendet die strukturierte Datei <code>persons.json</code>
        und verbindet sie fuer die Karte mit <code>locations.json</code>.
      </p>
    </div>
  `;
}

function renderLinks(person) {
  const links = person.record.links || {};
  const linkEntries = Object.entries(links).filter(([, field]) => getTypedValue(field));

  if (!linkEntries.length) {
    DOM.links.innerHTML = '<p class="text-body-secondary mb-0">Keine externen Links vorhanden.</p>';
    return;
  }

  const inlineLinks = linkEntries
    .map(([key, field]) => {
      const url = getTypedValue(field);
      const linkLabel = buildLinkLabel(key, field);

      return `
        <a
          href="${escapeAttribute(url)}"
          target="_blank"
          rel="noopener noreferrer"
          class="link-inline"
        >${linkLabel}</a>
      `;
    })
    .join('<span class="link-separator">, </span>');

  DOM.links.innerHTML = `
    <div class="metadata-item compact">
      <span class="metadata-label">Externe Links</span>
      <p class="metadata-value mb-0">${inlineLinks}</p>
    </div>
  `;
}

function buildLinkLabel(key, field) {
  const icon = LINK_ICONS[key];

  if (icon) {
    return `
      <span class="link-label-group" title="${escapeAttribute(field.label || icon.text)}">
        <img
          src="${escapeAttribute(icon.src)}"
          alt="${escapeAttribute(icon.alt)}"
          class="link-icon"
        >
        <span class="link-text">${escapeHtml(icon.text)}</span>
      </span>
    `;
  }

  return escapeHtml(field.label || formatLinkKey(key));
}

function formatLinkKey(key) {
  return key
    .split(/[_-]/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function renderMapForPerson(person) {
  const mapPlaces = collectPersonPlaces(person.record);
  renderMap(mapPlaces);

  if (!mapPlaces.length) {
    DOM.mapSummary.textContent = "Keine georeferenzierten Orte fuer diese Person vorhanden.";
    return;
  }

  const summary = [
    `${mapPlaces.length} Orte auf der Karte`,
    '<span class="marker-legend"><span class="legend-dot" style="background:#198754"></span>Geburt</span>',
    '<span class="marker-legend"><span class="legend-dot" style="background:#dc3545"></span>Tod</span>',
    '<span class="marker-legend"><span class="legend-dot" style="background:#0d6efd"></span>Wirkungsorte</span>',
  ].join(" ");

  DOM.mapSummary.innerHTML = summary;
}

function collectPersonPlaces(record) {
  const places = [];

  addLifeLocations(places, record.life?.birth?.location, "birth", "Geburtsort");
  addLifeLocations(places, record.life?.death?.location, "death", "Todesort");

  const activityField = record.life?.places_of_effect;
  const activities = getTypedValue(activityField);

  if (Array.isArray(activities)) {
    activities.forEach((entry) => {
      if (entry.type !== "ComplexType") {
        return;
      }

      const values = entry.value?.values || [];
      const temporal = values[0]?.value || "";
      const locationId = values[1]?.value || "";
      const institution = values[2]?.value || "";
      const role = values[3]?.value || "";

      const location = state.locationsById.get(locationId);
      if (!location || location.longitude === null || location.latitude === null) {
        return;
      }

      const parts = [temporal, institution, role].filter(Boolean);
      places.push({
        type: "activity",
        title: location.name,
        subtitle: parts.join(" | "),
        latitude: location.latitude,
        longitude: location.longitude,
      });
    });
  }

  return deduplicatePlaces(places);
}

function addLifeLocations(target, field, type, label) {
  const values = getTypedValue(field);
  if (!Array.isArray(values)) {
    return;
  }

  values.forEach((entry) => {
    const locationId = entry?.value;
    if (!locationId) {
      return;
    }

    const location = state.locationsById.get(locationId);
    if (!location || location.longitude === null || location.latitude === null) {
      return;
    }

    target.push({
      type,
      title: location.name,
      subtitle: label,
      latitude: location.latitude,
      longitude: location.longitude,
    });
  });
}

function deduplicatePlaces(places) {
  const seen = new Set();

  return places.filter((place) => {
    const key = [place.type, place.title, place.latitude, place.longitude, place.subtitle].join("|");
    if (seen.has(key)) {
      return false;
    }
    seen.add(key);
    return true;
  });
}

function setupMap() {
  state.map = L.map("person-map", {
    scrollWheelZoom: true,
  }).setView([20, 10], 2);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "&copy; OpenStreetMap contributors",
  }).addTo(state.map);
}

function renderMap(places) {
  state.mapLayers.forEach((layer) => layer.remove());
  state.mapLayers = [];

  if (!places.length) {
    DOM.mapEmptyState.classList.remove("d-none");
    state.map.setView([20, 10], 2);
    return;
  }

  DOM.mapEmptyState.classList.add("d-none");
  state.map.invalidateSize();

  const bounds = [];

  places.forEach((place) => {
    const marker = L.circleMarker([place.latitude, place.longitude], {
      radius: 8,
      color: MARKER_COLORS[place.type] || "#495057",
      fillColor: MARKER_COLORS[place.type] || "#495057",
      fillOpacity: 0.85,
      weight: 2,
    }).addTo(state.map);

    marker.bindPopup(`
      <strong>${escapeHtml(place.title)}</strong><br>
      <span>${escapeHtml(place.subtitle || "")}</span>
    `);

    state.mapLayers.push(marker);
    bounds.push([place.latitude, place.longitude]);
  });

  if (bounds.length === 1) {
    state.map.setView(bounds[0], 6);
  } else {
    state.map.fitBounds(bounds, { padding: [30, 30] });
  }
}

function getPreferredName(record) {
  return getTypedValue(record.name?.preferred);
}

function getTypedValue(fieldOrTypedValue) {
  if (!fieldOrTypedValue) {
    return null;
  }

  // Our leaf nodes have the shape { label, value }.
  if ("label" in fieldOrTypedValue && "value" in fieldOrTypedValue && fieldOrTypedValue.value?.type) {
    return getTypedValue(fieldOrTypedValue.value);
  }

  if (!fieldOrTypedValue.type) {
    return null;
  }

  if (fieldOrTypedValue.type === "List") {
    return (fieldOrTypedValue.value || []).map((entry) => getTypedValue(entry));
  }

  if (fieldOrTypedValue.type === "Object") {
    const result = {};
    Object.entries(fieldOrTypedValue.value || {}).forEach(([key, value]) => {
      result[key] = getTypedValue(value);
    });
    return result;
  }

  if (fieldOrTypedValue.type === "ComplexType") {
    return fieldOrTypedValue.value || null;
  }

  return fieldOrTypedValue.value;
}

function formatLifeEvent(eventObject) {
  if (!eventObject) {
    return "";
  }

  const dates = getTypedValue(eventObject.date);
  const locations = getTypedValue(eventObject.location);
  const dateText = Array.isArray(dates) ? dates.join(", ") : dates;
  const locationText = Array.isArray(locations) ? locations.join(", ") : locations;

  return [dateText, locationText].filter(Boolean).join(" | ");
}

function countListEntries(field) {
  const value = getTypedValue(field);
  return Array.isArray(value) ? value.length : 0;
}

function formatTypedValue(field) {
  const value = getTypedValue(field);

  if (Array.isArray(value)) {
    return value.join(", ");
  }

  if (value && typeof value === "object") {
    return JSON.stringify(value);
  }

  return value || "";
}

function showError(error) {
  DOM.loading.classList.add("d-none");
  DOM.error.classList.remove("d-none");
  DOM.error.textContent = `Beim Laden der Daten ist ein Fehler aufgetreten: ${error.message}`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function escapeAttribute(value) {
  return escapeHtml(value);
}
