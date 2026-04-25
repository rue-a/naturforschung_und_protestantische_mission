/* =====================================================
   map.js  —  pure view helpers for the Leaflet locations map
   ===================================================== */

// Asset base path, relative to html/locations.html
const LOC_ASSETS = "../assets";

/** Minimum zoom level at which placename labels are shown. */
const LABEL_MIN_ZOOM = 7;

/**
 * Marker style based on a normalised importance value t ∈ [0, 1].
 * Radius scales with √t from 4 to 14 px.
 * Hue interpolates from 210° (blue) → 20° (orange-red) as importance rises.
 * Zero-importance locations are rendered in a neutral grey.
 * @param {number} score
 * @param {number} maxScore
 * @returns {{ radius: number, fillColor: string, color: string, labelColor: string }}
 */
function _importanceMarkerStyle(score, maxScore) {
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
		labelColor: `hsl(${hue},80%,20%)`,
	};
}

/** Escape a value for safe HTML injection. */
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
		+ `<img src="${LOC_ASSETS}/wikidata_18x12.svg" alt="Wikidata" class="ref-icon wikidata-icon">`
		+ `</a>`;
}

/**
 * Return an HTML string for a Herrnhut icon linking to the persons page.
 * @param {string|null|undefined} id
 * @returns {string}
 */
function _herrnhutPersonIconHtml(id) {
	if (!id) return "";
	const href = `persons.html?personid=${encodeURIComponent(id)}`;
	return `<a href="${_esc(href)}" class="loc-wd-link">`
		+ `<img src="${LOC_ASSETS}/herrnhut_logo256x256.png" alt="Personenregister" class="ref-icon herrnhut-icon">`
		+ `</a>`;
}

/**
 * Initialise the Leaflet map with the CartoDB light basemap.
 * @returns {L.Map}
 */
function initMap() {
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
	return map;
}

/**
 * Create a Leaflet circle marker for a feature using precomputed style values.
 * Binds a permanent tooltip (label) coloured from the style; no event handlers attached.
 * @param {object} feature — GeoJSON/JSON-FG feature
 * @param {{ radius: number, fillColor: string, color: string, labelColor: string }} markerStyle
 * @returns {{ marker: L.CircleMarker, origStyle: object }}
 */
function createMarker(feature, markerStyle) {
	const { radius, fillColor, color, labelColor } = markerStyle;
	const [lng, lat] = feature.geometry.coordinates;
	const props = feature.properties ?? {};
	const origStyle = { color, weight: 1, fillOpacity: 0.75 };

	const marker = L.circleMarker([lat, lng], {
		radius,
		color,
		fillColor,
		fillOpacity: 0.75,
		weight: 1,
	}).bindTooltip(props.name ?? feature.id, {
		permanent: true,
		direction: "bottom",
		className: "loc-label",
		opacity: 0, // hidden until zoom threshold is reached
		offset: [0, radius + 2],
	});

	marker.on("tooltipopen", (e) => {
		e.tooltip.getElement().style.color = labelColor;
	});

	return { marker, origStyle };
}

/**
 * Show or hide placename labels on all markers.
 * @param {L.CircleMarker[]} markers
 * @param {boolean} show
 */
function updateLabels(markers, show) {
	for (const m of markers) m.getTooltip()?.setOpacity(show ? 1 : 0);
}

/**
 * Build the HTML content for the location sidebar.
 * @param {object} props     — feature.properties
 * @param {string} featureId — feature.id (fallback for name)
 * @returns {string} HTML string
 */
function buildSidebarContent(props, featureId) {
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
			html += `<li><span class="loc-person-name">${_esc(b.name)}${_herrnhutPersonIconHtml(b.id)}${_wikidataIconHtml(b.wikidata)}</span>`;
			if (b.date) html += `<span class="loc-person-meta">${_esc(b.date)}</span>`;
			html += `</li>`;
		}
		html += `</ul></section>`;
	}
	if (deaths.length) {
		html += `<section><h4>Todesfälle</h4><ul>`;
		for (const d of deaths) {
			html += `<li><span class="loc-person-name">${_esc(d.name)}${_herrnhutPersonIconHtml(d.id)}${_wikidataIconHtml(d.wikidata)}</span>`;
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
			html += `<span class="loc-person-name">${_esc(person.name)}${_herrnhutPersonIconHtml(person.id)}${_wikidataIconHtml(person.wikidata)}</span>`;
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

/** HTML string for the sidebar's default (no selection) hint. */
function sidebarHintHtml() {
	return '<p class="loc-sidebar-hint">Ort anklicken für Details.</p>';
}
