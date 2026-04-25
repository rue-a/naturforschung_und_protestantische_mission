/* =====================================================
   controller.js  —  wire model and view for the locations page
   ===================================================== */

// Path relative to html/locations.html
const LOCATIONS_DATA_URL = "../data/locations.json";

const SELECTED_STYLE = { color: "hsl(338, 100%, 68%)", weight: 4, fillOpacity: 1 };

document.addEventListener("DOMContentLoaded", async () => {
	const featureCollection = await loadLocations(LOCATIONS_DATA_URL);
	const features = featureCollection.features ?? [];

	const maxScore = Math.max(0, ...features.map((f) => _importanceScore(f.properties ?? {})));

	const map = initMap();
	const sidebar = document.getElementById("loc-sidebar");
	let selectedMarker = null;
	let selectedOrigStyle = null;
	const markers = [];
	const markerEntries = []; // { marker, featureId } for URL pre-selection
	const markerGroup = L.featureGroup();

	for (const feature of features) {
		if (!feature.geometry?.coordinates) continue;

		const props = feature.properties ?? {};
		const score = _importanceScore(props);
		const markerStyle = _importanceMarkerStyle(score, maxScore);
		const { marker, origStyle } = createMarker(feature, markerStyle);

		marker.on("click", (e) => {
			L.DomEvent.stopPropagation(e);
			if (selectedMarker) selectedMarker.setStyle(selectedOrigStyle);
			selectedOrigStyle = origStyle;
			selectedMarker = marker;
			marker.setStyle(SELECTED_STYLE);
			marker.bringToFront();
			sidebar.innerHTML = buildSidebarContent(props, feature.id);
			setLocationIdInUrl(feature.id);
		});

		marker.addTo(markerGroup);
		markers.push(marker);
		markerEntries.push({ marker, featureId: feature.id });
	}

	markerGroup.addTo(map);

	map.on("zoomend", () => updateLabels(markers, map.getZoom() >= LABEL_MIN_ZOOM));

	map.on("click", () => {
		if (selectedMarker) {
			selectedMarker.setStyle(selectedOrigStyle);
			selectedMarker = null;
			selectedOrigStyle = null;
		}
		setLocationIdInUrl(null);
		sidebar.innerHTML = sidebarHintHtml();
	});

	// Pre-select location from URL parameter
	const urlId = getLocationIdFromUrl();
	if (urlId) {
		const idx = markerEntries.findIndex(e => e.featureId === urlId);
		if (idx !== -1) markerEntries[idx].marker.fire("click");
	}

	if (markerGroup.getLayers().length) {
		map.fitBounds(markerGroup.getBounds(), { padding: [30, 30] });
	} else {
		map.setView([20, 0], 2);
	}
});
