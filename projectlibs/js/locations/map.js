/* =====================================================
   map.js  —  pure view helpers for the Leaflet locations map
   ===================================================== */

// Asset base path, relative to html/locations.html
const LOC_ASSETS = "../assets";

/** Minimum zoom level at which placename labels are shown. */
const LABEL_MIN_ZOOM = 7;

/**
 * Marker style based on a normalised events value t ∈ [0, 1].
 * Radius scales with √t from 4 to 14 px.
 * Hue interpolates from 210° (blue) → 20° (orange-red) as events rises.
 * Zero-events locations are rendered in a neutral grey.
 * @param {number} score
 * @param {number} maxScore
 * @returns {{ radius: number, fillColor: string, color: string, labelColor: string }}
 */
function _eventsMarkerStyle(score, maxScore) {
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

/**
 * Return a Wikidata icon link, or null if no URL.
 * @param {string|null|undefined} url
 * @returns {HTMLAnchorElement|null}
 */
function _wikidataIconLink(url) {
	if (!url) return null;
	const a = document.createElement("a");
	a.href = url;
	a.target = "_blank";
	a.rel = "noopener noreferrer";
	a.className = "loc-wd-link";

	const img = document.createElement("img");
	img.src = `${LOC_ASSETS}/wikidata_18x12.svg`;
	img.alt = "Wikidata";
	img.className = "ref-icon wikidata-icon";
	a.appendChild(img);
	return a;
}

/**
 * Return a Herrnhut icon link to the persons page, or null if no id.
 * @param {string|null|undefined} id
 * @returns {HTMLAnchorElement|null}
 */
function _herrnhutPersonIconLink(id) {
	if (!id) return null;
	const a = document.createElement("a");
	a.href = `persons.html?personid=${encodeURIComponent(id)}`;
	a.className = "loc-wd-link";

	const img = document.createElement("img");
	img.src = `${LOC_ASSETS}/herrnhut_logo256x256.png`;
	img.alt = "Personenregister";
	img.className = "ref-icon herrnhut-icon";
	a.appendChild(img);
	return a;
}

/**
 * Initialise the Leaflet map with the CartoDB light basemap.
 * @returns {L.Map}
 */
function initMap() {
	const map = L.map("map");
	L.tileLayer(
		"https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
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
 * Build the DOM content for the location sidebar.
 * @param {object} props     — feature.properties
 * @param {string} featureId — feature.id (fallback for name)
 * @returns {HTMLDivElement}
 */
function buildSidebarContent(props, featureId) {
	const name = props.name ?? featureId;
	const imp = props.events ?? {};
	const births = imp.births ?? [];
	const deaths = imp.deaths ?? [];
	const poe = imp.places_of_effect ?? [];

	const root = document.createElement("div");
	root.className = "loc-content";

	const title = document.createElement("h2");
	title.textContent = name;
	const wdForTitle = _wikidataIconLink(props.wikidata);
	if (wdForTitle) title.appendChild(wdForTitle);
	root.appendChild(title);

	if (props.description) {
		const desc = document.createElement("p");
		desc.className = "loc-desc";
		desc.textContent = props.description;
		root.appendChild(desc);
	}

	if (births.length) root.appendChild(_personEventSection("Geburten", births));
	if (deaths.length) root.appendChild(_personEventSection("Todesf\u00e4lle", deaths));
	if (poe.length) root.appendChild(_poeSection(poe));

	if (!births.length && !deaths.length && !poe.length) {
		const empty = document.createElement("p");
		empty.className = "loc-content-empty";
		empty.textContent = "Keine Personen verkn\u00fcpft.";
		root.appendChild(empty);
	}

	return root;
}

function _personEventSection(titleText, items) {
	const section = document.createElement("section");
	const h = document.createElement("h3");
	h.textContent = titleText;
	section.appendChild(h);

	const temporalSortKey = (value) => {
		if (!value) return "";
		// For periods, sort by the start part if present.
		const start = String(value).split("/")[0] || String(value).split("/")[1] || "";
		return start.replace(/[?~%]/g, "");
	};

	const orderedItems = [...items].sort((a, b) => {
		const ta = temporalSortKey(a.date);
		const tb = temporalSortKey(b.date);
		if (!ta && !tb) return 0;
		if (!ta) return 1;
		if (!tb) return -1;
		return ta.localeCompare(tb);
	});

	const ul = document.createElement("ul");
	for (const item of orderedItems) {
		const li = document.createElement("li");
		const nameSpan = document.createElement("span");
		nameSpan.className = "loc-person-name";
		nameSpan.appendChild(document.createTextNode(item.name ?? ""));

		const hh = _herrnhutPersonIconLink(item.id);
		if (hh) nameSpan.appendChild(hh);
		const wd = _wikidataIconLink(item.wikidata);
		if (wd) nameSpan.appendChild(wd);

		li.appendChild(nameSpan);

		if (item.date_formatted) {
			const meta = document.createElement("span");
			meta.className = "loc-person-meta";
			meta.textContent = item.date_formatted;
			li.appendChild(meta);
		}

		ul.appendChild(li);
	}
	section.appendChild(ul);
	return section;
}

function _poeSection(poe) {
	const section = document.createElement("section");
	const h = document.createElement("h3");
	h.textContent = "Wirkende Personen";
	section.appendChild(h);

	// Group entries by person ID so repeated visits appear under one header.
	const byPerson = [];
	const indexById = {};
	for (const p of poe) {
		const key = p.id ?? `${p.name ?? ""}-${byPerson.length}`;
		if (!(key in indexById)) {
			indexById[key] = byPerson.length;
			byPerson.push({ id: p.id, name: p.name, wikidata: p.wikidata, stints: [] });
		}
		const parts = [p.temporal_formatted, p.institution, p.occupation].filter(Boolean);
		if (parts.length) byPerson[indexById[key]].stints.push(parts.join(" \u00b7 "));
	}

	const ul = document.createElement("ul");
	ul.className = "loc-poe-list";

	for (const person of byPerson) {
		const li = document.createElement("li");
		li.className = "loc-poe-group";

		const nameSpan = document.createElement("span");
		nameSpan.className = "loc-person-name";
		nameSpan.appendChild(document.createTextNode(person.name ?? ""));

		const hh = _herrnhutPersonIconLink(person.id);
		if (hh) nameSpan.appendChild(hh);
		const wd = _wikidataIconLink(person.wikidata);
		if (wd) nameSpan.appendChild(wd);

		li.appendChild(nameSpan);

		if (person.stints.length) {
			const stints = document.createElement("ul");
			stints.className = "loc-poe-stints";
			for (const stint of person.stints) {
				const sLi = document.createElement("li");
				sLi.textContent = stint;
				stints.appendChild(sLi);
			}
			li.appendChild(stints);
		}

		ul.appendChild(li);
	}

	section.appendChild(ul);
	return section;
}

/** DOM node for the sidebar's default (no selection) hint. */
function sidebarHintHtml() {
	const hint = document.createElement("p");
	hint.className = "loc-sidebar-hint";
	hint.textContent = "Ort anklicken für Details.";
	return hint;
}

/**
 * DOM content for a hexbin containing multiple locations.
 * @param {Array<{ feature: object, score: number }>} points
 * @returns {HTMLDivElement}
 */
function buildHexbinSidebarContent(points) {
	const root = document.createElement("div");
	root.className = "loc-content";

	const title = document.createElement("h2");
	title.textContent = `${points.length} Orte im Hexbin`;
	root.appendChild(title);

	const hint = document.createElement("p");
	hint.className = "loc-desc";
	hint.textContent = "Zoome weiter hinein oder wähle einen einzelnen Ort aus dem Personen- oder Ortskontext.";
	root.appendChild(hint);

	const section = document.createElement("section");
	const h = document.createElement("h3");
	h.textContent = "Enthaltene Orte";
	section.appendChild(h);

	const ul = document.createElement("ul");
	const ordered = [...points].sort((a, b) => (b.score ?? 0) - (a.score ?? 0));
	for (const p of ordered) {
		const li = document.createElement("li");
		const name = p.feature?.properties?.name ?? p.feature?.id ?? "Unbenannter Ort";
		li.textContent = `${name} (${p.score ?? 0})`;
		ul.appendChild(li);
	}
	section.appendChild(ul);
	root.appendChild(section);

	return root;
}
