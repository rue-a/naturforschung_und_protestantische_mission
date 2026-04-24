/* =====================================================
   map.js  —  Leaflet locations map
   ===================================================== */

// Asset base path, relative to html/locations.html
const LOC_ASSETS = "../assets";

/** Minimum zoom level at which placename labels are shown. */
const LABEL_MIN_ZOOM = 7;

/**
 * Total importance score for a location: sum of persons born, died, or active there.
 * @param {object} props  — feature.properties
 * @returns {number}
 */
function _importanceScore(props) {
	const imp = props.importance ?? {};
	return (
		(imp.births?.length ?? 0) +
		(imp.deaths?.length ?? 0) +
		(imp.places_of_effect?.length ?? 0)
	);
}

/**
 * Marker style based on a normalised importance value t ∈ [0, 1].
 * Radius scales with √t from 4 to 14 px.
 * Hue interpolates from 210° (blue) → 20° (orange-red) as importance rises.
 * Zero-importance locations are rendered in a neutral grey.
 * @param {number} score
 * @param {number} maxScore
 * @returns {{ radius: number, fillColor: string, color: string, labelColor: string }}
 */
function _markerStyle(score, maxScore) {
	if (score === 0 || maxScore === 0) {
		return {
			radius: 4,
			fillColor: "hsl(0,0%,65%)",
			color: "hsl(0,0%,40%)",
			labelColor: "hsl(0,0%,22%)",
		};
	}
	const t = Math.sqrt(score / maxScore);
	const radius = 4 + t * 10;
	const hue = Math.round(210 - t * 190); // 210 (blue) → 20 (orange-red)
	return {
		radius,
		fillColor: `hsl(${hue},70%,45%)`,
		color: `hsl(${hue},70%,28%)`,
		labelColor: `hsl(${hue},80%,20%)`,  // same hue, higher saturation, much darker
	};
}

/** Escape a value for safe HTML injection into popups. */
function _esc(val) {
	return String(val ?? "")
		.replace(/&/g, "&amp;")
		.replace(/</g, "&lt;")
		.replace(/>/g, "&gt;")
		.replace(/"/g, "&quot;");
}

/**
 * Return an HTML string for a Wikidata icon link, or empty string if no URL.
 * @param {string|null|undefined} url
 * @returns {string}
 */
function _wikidataIconHtml(url) {
	if (!url) return "";
	return `<a href="${_esc(url)}" target="_blank" rel="noopener" class="loc-wd-link">`
		+ `<img src="${LOC_ASSETS}/wikidata_18x12.svg" alt="Wikidata" class="wikidata-icon loc-wd-icon">`
		+ `</a>`;
}

/**
 * Build the HTML content for the location sidebar.
 * Shows place name (linked to Wikidata if available), description, and
 * lists persons born, who died, and who were active at this location.
 * @param {object} props     — feature.properties
 * @param {string} featureId — feature.id (fallback for name)
 * @returns {string} HTML string
 */
function _buildSidebarContent(props, featureId) {
	const name = props.name ?? featureId;
	const imp = props.importance ?? {};
	const births = imp.births ?? [];
	const deaths = imp.deaths ?? [];
	const poe = imp.places_of_effect ?? [];

	const nameHtml = `${_esc(name)} ${_wikidataIconHtml(props.wikidata)}`;

	let html = `<div class="loc-content"><h2>${nameHtml}</h2>`;

	if (props.description) {
		html += `<p class="loc-desc">${_esc(props.description)}</p>`;
	}

	if (births.length) {
		html += `<section><h4>Geburten</h4><ul>`;
		for (const b of births) {
			html += `<li><span class="loc-person-name">${_esc(b.name)}${_wikidataIconHtml(b.wikidata)}</span>`;
			if (b.date) html += `<span class="loc-person-meta">${_esc(b.date)}</span>`;
			html += `</li>`;
		}
		html += `</ul></section>`;
	}
	if (deaths.length) {
		html += `<section><h4>Todesfälle</h4><ul>`;
		for (const d of deaths) {
			html += `<li><span class="loc-person-name">${_esc(d.name)}${_wikidataIconHtml(d.wikidata)}</span>`;
			if (d.date) html += `<span class="loc-person-meta">${_esc(d.date)}</span>`;
			html += `</li>`;
		}
		html += `</ul></section>`;
	}
	if (poe.length) {
		// Group entries by person ID so repeated visits appear under one header
		const byPerson = [];
		const indexById = {};
		for (const p of poe) {
			if (!(p.id in indexById)) {
				indexById[p.id] = byPerson.length;
				byPerson.push({ id: p.id, name: p.name, wikidata: p.wikidata, stints: [] });
			}
			const parts = [p.temporal, p.institution, p.occupation].filter(Boolean);
			if (parts.length) byPerson[indexById[p.id]].stints.push(parts.join(" · "));
		}
		html += `<section><h4>Wirkende Personen</h4><ul class="loc-poe-list">`;
		for (const person of byPerson) {
			html += `<li class="loc-poe-group">`;
			html += `<span class="loc-person-name">${_esc(person.name)}${_wikidataIconHtml(person.wikidata)}</span>`;
			if (person.stints.length) {
				html += `<ul class="loc-poe-stints">`;
				for (const stint of person.stints) {
					html += `<li>${_esc(stint)}</li>`;
				}
				html += `</ul>`;
			}
			html += `</li>`;
		}
		html += `</ul></section>`;
	}
	if (!births.length && !deaths.length && !poe.length) {
		html += `<p class="loc-content-empty">Keine Personen verknüpft.</p>`;
	}
	html += `</div>`;
	return html;
}

/**
 * Initialise the Leaflet map and render all location features as circle markers.
 * - Markers are scaled and colourised by importance.
 * - Permanent placename labels are shown from zoom ≥ LABEL_MIN_ZOOM.
 *   Implemented via Leaflet's built-in permanent tooltip, the equivalent of the
 *   archived leaflet/leaflet.label plugin (whose functionality merged into Leaflet core).
 * - Clicking a marker opens a popup listing persons born, died, or active there.
 * Locations without geometry coordinates are silently skipped.
 * @param {object} featureCollection  — JSON-FG FeatureCollection
 */
function renderLocationsMap(featureCollection) {
	const map = L.map("map");

	L.tileLayer(
		"https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
		{
			attribution:
				'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors ' +
				'&copy; <a href="https://carto.com/">CartoDB</a>',
			subdomains: "abcd",
			maxZoom: 19,
		}
	).addTo(map);

	const features = featureCollection.features ?? [];
	const maxScore = Math.max(
		0,
		...features.map((f) => _importanceScore(f.properties ?? {}))
	);

	const sidebar = document.getElementById("loc-sidebar");
	let selectedMarker = null;
	let selectedOrigStyle = null;

	const markerGroup = L.featureGroup();
	const markers = [];

	for (const feature of features) {
		const coords = feature.geometry?.coordinates;
		if (!coords) continue;

		const [lng, lat] = coords;
		const props = feature.properties ?? {};
		const score = _importanceScore(props);
		const { radius, fillColor, color, labelColor } = _markerStyle(score, maxScore);
		const origStyle = { color, weight: 1, fillOpacity: 0.75 };

		const marker = L.circleMarker([lat, lng], {
			radius,
			color,
			fillColor,
			fillOpacity: 0.75,
			weight: 1,
		})
			.bindTooltip(props.name ?? feature.id, {
				permanent: true,
				direction: "bottom",
				className: "loc-label",
				opacity: 0, // hidden until zoom threshold is reached
				offset: [0, radius + 2], // push label below the marker edge
			});

		// Apply per-marker hue-derived color to the label element once it exists
		marker.on("tooltipopen", (e) => {
			e.tooltip.getElement().style.color = labelColor;
		});

		// Click: highlight this marker and populate the sidebar
		marker.on("click", (e) => {
			L.DomEvent.stopPropagation(e);
			if (selectedMarker) {
				selectedMarker.setStyle(selectedOrigStyle);
			}
			selectedOrigStyle = origStyle;
			selectedMarker = marker;
			marker.setStyle({
				color: "hsl(338, 100%, 68%)",
				weight: 4,
				fillOpacity: 1,
			});
			marker.bringToFront();
			sidebar.innerHTML = _buildSidebarContent(props, feature.id);
		});

		marker.addTo(markerGroup);
		markers.push(marker);
	}

	markerGroup.addTo(map);

	// Show/hide labels depending on current zoom level
	const _updateLabels = () => {
		const show = map.getZoom() >= LABEL_MIN_ZOOM;
		for (const m of markers) m.getTooltip()?.setOpacity(show ? 1 : 0);
	};
	map.on("zoomend", _updateLabels);

	map.on("click", () => {
		if (selectedMarker) {
			selectedMarker.setStyle(selectedOrigStyle);
			selectedMarker = null;
			selectedOrigStyle = null;
		}
		sidebar.innerHTML = '<p class="loc-sidebar-hint">Ort anklicken für Details.</p>';
	});

	if (markerGroup.getLayers().length) {
		map.fitBounds(markerGroup.getBounds(), { padding: [30, 30] });
	} else {
		map.setView([20, 0], 2);
	}
}
