/* =====================================================
   map.js  —  Leaflet life trajectory map
   ===================================================== */

let _trajectoryMap = null;

// Colour per featureType
const TRAJECTORY_COLORS = {
	birth: "#2a9d4e",   /* green  */
	death: "#c0392b",   /* red    */
	place_of_effect: "#2563eb",   /* blue   */
};

const TRAJECTORY_LABELS = {
	birth: "Geburt",
	death: "Tod",
	place_of_effect: "Wirkungsort",
};

/**
 * Destroy any existing map instance and create a fresh one in #trajectory-map.
 * Returns the new Leaflet map object.
 */
function _initMap() {
	if (_trajectoryMap) {
		_trajectoryMap.remove();
		_trajectoryMap = null;
	}
	_trajectoryMap = L.map("trajectory-map");
	L.tileLayer(
		"https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
		{
			attribution:
				'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors ' +
				'&copy; <a href="https://carto.com/">CartoDB</a>',
			subdomains: "abcd",
			maxZoom: 19,
		}
	).addTo(_trajectoryMap);
	return _trajectoryMap;
}

/**
 * Render a person's life_trajectory GeoJSON-FG FeatureCollection on the map.
 * Draws coloured circle markers plus a dashed polyline connecting all points
 * in the order they appear in the features array.
 * @param {object|null} trajectory
 */
function renderTrajectory(trajectory) {
	const map = _initMap();
	const features = trajectory?.features ?? [];
	if (!features.length) return;

	const latLngs = [];
	const clusterGroup = L.markerClusterGroup();

	for (const feature of features) {
		const coords = feature.geometry?.coordinates;
		if (!coords) continue;

		const [lng, lat] = coords;
		const color = TRAJECTORY_COLORS[feature.featureType] ?? "#888888";
		const typeLabel = TRAJECTORY_LABELS[feature.featureType] ?? feature.featureType;
		const place = feature.properties?.place_name ?? "";
		const time =
			feature.time?.date ??
			(feature.time?.interval ?? []).filter(Boolean).join(" – ") ??
			"";

		const institution = feature.properties?.institution ?? "";
		const occupation = feature.properties?.occupation ?? "";
		const popupLines = [
			`<strong>${typeLabel}</strong>`,
			place,
			time,
			[institution, occupation].filter(Boolean).join(", "),
		].filter(Boolean);

		L.circleMarker([lat, lng], {
			radius: 6,
			color: color,
			fillColor: color,
			fillOpacity: 0.85,
			weight: 1.5,
		})
			.bindPopup(popupLines.join("<br>"))
			.addTo(clusterGroup);

		latLngs.push([lat, lng]);
	}

	map.addLayer(clusterGroup);
	map.fitBounds(L.latLngBounds(latLngs), { padding: [24, 24] });
}
