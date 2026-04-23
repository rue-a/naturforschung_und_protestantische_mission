/* =====================================================
   map.js  —  Leaflet locations map
   ===================================================== */

/**
 * Initialise the Leaflet map and render all location features as circle markers.
 * Locations without geometry coordinates are silently skipped.
 * @param {object} featureCollection  — JSON-FG FeatureCollection
 */
function renderLocationsMap(featureCollection) {
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

	const features = featureCollection.features ?? [];
	const markerGroup = L.featureGroup();

	for (const feature of features) {
		const coords = feature.geometry?.coordinates;
		if (!coords) continue;

		const [lng, lat] = coords;
		const props = feature.properties ?? {};

		L.circleMarker([lat, lng], {
			radius: 6,
			color: "#1e1e1e",
			fillColor: "#1e1e1e",
			fillOpacity: 0.45,
			weight: 1,
		})
			.bindTooltip(props.name ?? feature.id, { sticky: true })
			.addTo(markerGroup);
	}

	markerGroup.addTo(map);

	if (markerGroup.getLayers().length) {
		map.fitBounds(markerGroup.getBounds(), { padding: [30, 30] });
	} else {
		map.setView([20, 0], 2);
	}
}
