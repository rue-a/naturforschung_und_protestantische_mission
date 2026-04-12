window.AppView = (() => {
  const { state, MARKER_COLORS, LINK_ICONS } = window.AppModel;
  const MORAVIAN_MEMBERSHIP_LABELS = {
    "ja(a)": "qua Geburt und Erziehung, in einer Herrnhuter Gemeinschaft bzw. von Herrnhuter Eltern geboren und aufgewachsen",
    "ja(b)": "als Erwachsene aufgenommen, z.B. Konvertitien oder Missionierte",
    "ja(c)": "Übernahme von kirchlichen Ämtern innerhalb der Brüdergemeine",
    "ja(d)": "Übernahme von Ämtern im Erziehungswesen der Brüdergemeine",
    "nein(a)": "ausgetreten",
    "nein(b)": "aber wichtig im Netzwerk",
    "nein(c)": "um Verwechslung auszuschließen",
    unbekannt: "Zugehörigkeit kann nicht ausgeschlossen werden.",
  };

  const DOM = {
    loading: document.getElementById("loading-state"),
    appShell: document.getElementById("app-shell"),
    searchInput: document.getElementById("person-search"),
    browser: document.getElementById("person-browser"),
    metadata: document.getElementById("person-metadata"),
    article: document.getElementById("person-article"),
    links: document.getElementById("person-links"),
    mapSummary: document.getElementById("map-summary"),
    mapContainer: document.getElementById("person-map"),
    mapPopup: document.getElementById("map-popup"),
    mapEmptyState: document.getElementById("map-empty-state"),
  };

  function renderBrowser() {
    DOM.browser.innerHTML = "";

    if (state.filteredPersonIds.length === 0) {
      DOM.browser.innerHTML =
        '<div class="list-group-item text-body-secondary">Keine Person gefunden.</div>';
      return;
    }

    state.filteredPersonIds.forEach((personId) => {
      const record = state.personsById[personId];
      const name = record.name.preferred.value.value;
      const button = document.createElement("button");
      button.type = "button";
      button.className =
        "list-group-item list-group-item-action d-flex justify-content-between align-items-start";

      if (personId === state.selectedPersonId) {
        button.classList.add("active");
      }

      button.innerHTML = `
        <div>
          <div class="fw-semibold">${escapeHtml(name)}</div>
          <div class="small ${personId === state.selectedPersonId ? "text-white-50" : "text-body-secondary"}">${escapeHtml(personId)}</div>
        </div>
      `;

      button.addEventListener("click", () => {
        window.AppController.selectPerson(personId);
      });

      DOM.browser.appendChild(button);
    });
  }

  function renderSelectedPerson() {
    if (!state.selectedPersonId) {
      DOM.metadata.innerHTML = "";
      DOM.article.innerHTML = "";
      DOM.links.innerHTML = "";
      renderMap([]);
      DOM.mapSummary.textContent = "Keine Person ausgewählt.";
      return;
    }

    const record = state.personsById[state.selectedPersonId];
    renderMetadata(state.selectedPersonId, record);
    renderArticle(state.selectedPersonId, record);
    renderLinks(record);
    renderMapForPerson(record);
  }

  function renderMetadata(personId, record) {
    const preferredName = record.name.preferred.value.value;
    const metadataItems = [
      [record.name.preferred.label, preferredName],
      [
        "member_of_moravians" in record ? record.member_of_moravians.label : "",
        "member_of_moravians" in record ? formatMoravianMembership(record.member_of_moravians.value) : "",
      ],
      [
        "birth" in record ? "Geburt" : "",
        "birth" in record ? formatLifeEventValue(record.birth) : "",
      ],
      [
        "death" in record ? "Tod" : "",
        "death" in record ? formatLifeEventValue(record.death) : "",
      ],
    ].filter(([label, value]) => label && value);

    DOM.metadata.innerHTML = metadataItems
      .map(
        ([label, value]) => `
          <div class="metadata-item compact">
            <span class="metadata-label">${escapeHtml(label)}</span>
            ${renderMetadataValue(value)}
          </div>
        `
      )
      .join("");
  }

  function renderArticle(personId, record) {
    const preferredName = record.name.preferred.value.value;
    const botanySections = buildBotanySections(record);
    const activityCount = record.life_trajectory.features.filter(
      (feature) => feature.featureType === "place_of_effect"
    ).length;

    DOM.article.innerHTML = `
      <h2 class="h3 mb-0">${escapeHtml(preferredName)}</h2>
      <p class="lead mb-0">
        Die folgende Übersicht zieht Informationen direkt aus dem botanischen Block der strukturierten Personendaten.
      </p>
      <div class="article-placeholder">
        <p class="mb-2">
          <strong>${escapeHtml(preferredName)}</strong> ist im aktuellen Datensatz als eigenstaendige Person erfasst.
          Die strukturierte Ansicht links und rechts kann bereits fuer Recherche, Verknuepfungen und kuratorische Arbeit genutzt werden.
        </p>
        <p class="mb-0">
          Erfasste Wirkungsorte: ${escapeHtml(String(activityCount))}.
        </p>
      </div>
      ${botanySections}
      <div>
        <h3 class="h6 text-body-secondary">Aktueller Stand</h3>
        <p class="mb-0">
          Der Personenbrowser verwendet die strukturierte Datei <code>geopersons.json</code>.
        </p>
      </div>
    `;
  }

  function buildBotanySections(record) {
    if (!("botany" in record)) {
      return `
        <div>
          <h3 class="h6 text-body-secondary">Botanik</h3>
          <p class="mb-0">Keine botanischen Angaben vorhanden.</p>
        </div>
      `;
    }

    const sections = Object.values(record.botany)
      .filter((field) => field && field.value)
      .map((field) => {
        const value = formatBotanyFieldValue(field);
        return `
          <div class="mb-3">
            <h3 class="h6 text-body-secondary">${escapeHtml(field.label)}</h3>
            ${renderArticleValue(value)}
          </div>
        `;
      })
      .join("");

    if (!sections) {
      return `
        <div>
          <h3 class="h6 text-body-secondary">Botanik</h3>
          <p class="mb-0">Keine botanischen Angaben vorhanden.</p>
        </div>
      `;
    }

    return sections;
  }

  function formatBotanyFieldValue(field) {
    if (field.value.type !== "List") {
      return window.AppModel.formatTypedValue(field.value);
    }

    return field.value.value.map((entry) =>
      typeof entry === "object" ? entry.value : entry
    );
  }

  function renderArticleValue(value) {
    if (Array.isArray(value)) {
      return `
        <ul class="article-list mb-0">
          ${value.map((entry) => `<li>${escapeHtml(String(entry))}</li>`).join("")}
        </ul>
      `;
    }

    return `<p class="mb-0">${escapeHtml(String(value))}</p>`;
  }

  function renderLinks(record) {
    const linkEntries = Object.entries(record.links).filter(([, field]) => field);

    if (linkEntries.length === 0) {
      DOM.links.innerHTML =
        '<p class="text-body-secondary mb-0">Keine externen Links vorhanden.</p>';
      return;
    }

    const inlineLinks = linkEntries
      .map(([key, field]) => {
        const url = field.value.value;
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
        <span class="link-label-group" title="${escapeAttribute(field.label)}">
          <img
            src="${escapeAttribute(icon.src)}"
            alt="${escapeAttribute(icon.alt)}"
            class="link-icon"
          >
          <span class="link-text">${escapeHtml(icon.text)}</span>
        </span>
      `;
    }

    return escapeHtml(field.label);
  }

  function formatMoravianMembership(typedValue) {
    return typedValue.value.map(
      (entry) => MORAVIAN_MEMBERSHIP_LABELS[entry.value] || entry.value
    );
  }

  function formatLifeEventValue(eventRecord) {
    const parts = [
      appendNotes(
        "date" in eventRecord ? eventRecord.date.value.value : "",
        "date_notes" in eventRecord ? eventRecord.date_notes.value.value : ""
      ),
      appendNotes(
        formatLocationField(eventRecord),
        "location_notes" in eventRecord ? eventRecord.location_notes.value.value : ""
      ),
    ].filter(Boolean);

    return parts.join(" | ");
  }

  function formatLocationField(eventRecord) {
    if (!("location" in eventRecord)) {
      return "";
    }

    return eventRecord.location.value.value;
  }

  function appendNotes(value, notes) {
    if (!value) {
      return "";
    }

    if (!notes) {
      return value;
    }

    return `${value} (${notes})`;
  }

  function renderMetadataValue(value) {
    if (Array.isArray(value)) {
      return `
        <ul class="metadata-list mb-0">
          ${value.map((entry) => `<li>${escapeHtml(String(entry))}</li>`).join("")}
        </ul>
      `;
    }

    return `<p class="metadata-value mb-0">${escapeHtml(String(value))}</p>`;
  }

  function renderMapForPerson(record) {
    const places = window.AppModel.collectPersonPlaces(record);
    renderMap(places);

    if (places.length === 0) {
      DOM.mapSummary.textContent =
        "Keine georeferenzierten Orte fuer diese Person vorhanden.";
      return;
    }

    DOM.mapSummary.innerHTML = [
      `${places.length} Orte auf der Karte`,
      '<span class="marker-legend"><span class="legend-dot" style="background:#198754"></span>Geburt</span>',
      '<span class="marker-legend"><span class="legend-dot" style="background:#dc3545"></span>Tod</span>',
      '<span class="marker-legend"><span class="legend-dot" style="background:#0d6efd"></span>Wirkungsorte</span>',
    ].join(" ");
  }

  function setupMap() {
    state.mapSource = new ol.source.Vector();

    const vectorLayer = new ol.layer.Vector({
      source: state.mapSource,
      style: (feature) =>
        new ol.style.Style({
          image: new ol.style.Circle({
            radius: 8,
            fill: new ol.style.Fill({
              color: MARKER_COLORS[feature.get("type")] || "#495057",
            }),
            stroke: new ol.style.Stroke({
              color: "#ffffff",
              width: 2,
            }),
          }),
        }),
    });

    state.mapOverlay = new ol.Overlay({
      element: DOM.mapPopup,
      positioning: "bottom-center",
      offset: [0, -12],
      stopEvent: false,
    });

    state.map = new ol.Map({
      target: "person-map",
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(),
        }),
        vectorLayer,
      ],
      overlays: [state.mapOverlay],
      view: new ol.View({
        center: ol.proj.fromLonLat([10, 20]),
        zoom: 2,
      }),
    });

    state.map.on("singleclick", (event) => {
      const feature = state.map.forEachFeatureAtPixel(
        event.pixel,
        (candidate) => candidate
      );

      if (!feature) {
        hidePopup();
        return;
      }

      showPopup(event.coordinate, feature.get("title"), feature.get("subtitle"));
    });
  }

  function renderMap(places) {
    state.mapSource.clear();
    hidePopup();

    if (places.length === 0) {
      DOM.mapEmptyState.classList.remove("d-none");
      state.map.getView().setCenter(ol.proj.fromLonLat([10, 20]));
      state.map.getView().setZoom(2);
      return;
    }

    DOM.mapEmptyState.classList.add("d-none");
    const features = places.map((place) => {
      const feature = new ol.Feature({
        geometry: new ol.geom.Point(
          ol.proj.fromLonLat([place.longitude, place.latitude])
        ),
        type: place.type,
        title: place.title,
        subtitle: place.subtitle,
      });
      return feature;
    });

    state.mapSource.addFeatures(features);

    const extent = state.mapSource.getExtent();
    if (features.length === 1) {
      state.map.getView().setCenter(
        ol.proj.fromLonLat([places[0].longitude, places[0].latitude])
      );
      state.map.getView().setZoom(6);
      return;
    }

    state.map.getView().fit(extent, {
      padding: [30, 30, 30, 30],
      maxZoom: 6,
    });
  }

  function showPopup(coordinate, title, subtitle) {
    DOM.mapPopup.innerHTML = `
      <strong>${escapeHtml(title)}</strong><br>
      <span>${escapeHtml(subtitle)}</span>
    `;
    DOM.mapPopup.classList.remove("d-none");
    state.mapOverlay.setPosition(coordinate);
  }

  function hidePopup() {
    DOM.mapPopup.classList.add("d-none");
    state.mapOverlay.setPosition(undefined);
  }

  function showApp() {
    DOM.loading.classList.add("d-none");
    DOM.appShell.classList.remove("d-none");
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

  return {
    DOM,
    setupMap,
    renderBrowser,
    renderSelectedPerson,
    showApp,
  };
})();
