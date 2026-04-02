window.AppView = (() => {
  const { state, MARKER_COLORS, LINK_ICONS } = window.AppModel;

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
      [record.id.label, personId],
      [
        "surname" in record.name ? record.name.surname.label : "",
        "surname" in record.name ? record.name.surname.value.value : "",
      ],
      [
        "given_name" in record.name ? record.name.given_name.label : "",
        "given_name" in record.name ? record.name.given_name.value.value : "",
      ],
      [
        "member_of_moravians" in record ? record.member_of_moravians.label : "",
        "member_of_moravians" in record ? window.AppModel.formatTypedValue(record.member_of_moravians.value) : "",
      ],
      [
        "birth" in record.life_trajectory ? record.life_trajectory.birth.date.label : "",
        "birth" in record.life_trajectory
          ? window.AppModel.formatLifeEvent(record.life_trajectory.birth)
          : "",
      ],
      [
        "death" in record.life_trajectory ? record.life_trajectory.death.date.label : "",
        "death" in record.life_trajectory
          ? window.AppModel.formatLifeEvent(record.life_trajectory.death)
          : "",
      ],
    ].filter(([label, value]) => label && value);

    DOM.metadata.innerHTML = metadataItems
      .map(
        ([label, value]) => `
          <div class="metadata-item compact">
            <span class="metadata-label">${escapeHtml(label)}</span>
            <p class="metadata-value mb-0">${escapeHtml(String(value))}</p>
          </div>
        `
      )
      .join("");
  }

  function renderArticle(personId, record) {
    const preferredName = record.name.preferred.value.value;
    const focusText =
      "focuses" in record.botany
        ? window.AppModel.formatTypedValue(record.botany.focuses.value)
        : "noch nicht erfasst";
    const activityCount =
      "places_of_effect" in record.life_trajectory
        ? record.life_trajectory.places_of_effect.value.value.length
        : 0;

    DOM.article.innerHTML = `
      <h2 class="h3 mb-0">${escapeHtml(preferredName)}</h2>
      <p class="lead mb-0">
        Diese Spalte ist als Platzhalter fuer einen spaeteren biografischen Artikel gedacht.
        Schon jetzt kann sie genutzt werden, um eine automatisch erzeugte Kurzansicht zu zeigen.
      </p>
      <div class="article-placeholder">
        <p class="mb-2">
          <strong>${escapeHtml(preferredName)}</strong> ist im aktuellen Datensatz als eigenstaendige Person erfasst.
          Die strukturierte Ansicht links und rechts kann bereits fuer Recherche, Verknuepfungen und kuratorische Arbeit genutzt werden.
        </p>
        <p class="mb-2">
          Botanische Foki: ${escapeHtml(String(focusText))}.
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

    if (places.length === 0) {
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
        <span>${escapeHtml(place.subtitle)}</span>
      `);

      state.mapLayers.push(marker);
      bounds.push([place.latitude, place.longitude]);
    });

    if (bounds.length === 1) {
      state.map.setView(bounds[0], 6);
      return;
    }

    state.map.fitBounds(bounds, { padding: [30, 30] });
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
