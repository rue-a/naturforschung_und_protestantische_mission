/* =====================================================
   controller.js  —  wire model and view for the locations page
   ===================================================== */

// Path relative to html/locations.html
const LOCATIONS_DATA_URL = "../data/locations.json";

const SELECTED_STYLE = { color: "hsl(338, 100%, 68%)", weight: 4, fillOpacity: 1 };

document.addEventListener("DOMContentLoaded", async () => {
	const featureCollection = await loadLocations(LOCATIONS_DATA_URL);
	const features = featureCollection.features ?? [];

	const maxScore = Math.max(0, ...features.map((f) => _eventsScore(f.properties ?? {})));

	const map = initMap();
	const sidebar = document.getElementById("loc-sidebar");

	if (typeof L === "undefined" || typeof L.hexbinLayer !== "function") {
		console.error("Leaflet hexbin plugin not loaded: ensure Leaflet, d3, d3-hexbin and leaflet-d3 scripts are loaded in this order.");
		sidebar.replaceChildren(sidebarHintHtml());
		return;
	}

	const points = [];
	const byId = {};
	for (const feature of features) {
		const coords = feature.geometry?.coordinates;
		if (!coords) continue;
		const score = _eventsScore(feature.properties ?? {});
		const point = {
			lng: coords[0],
			lat: coords[1],
			score,
			feature,
		};
		points.push(point);
		byId[feature.id] = point;
	}

	const colorFor = (value) => _eventsMarkerStyle(value, maxScore).fillColor;
	const unwrapPoint = (p) => p?.o ?? p;
	const binScore = (bin) => d3.sum(bin, (p) => unwrapPoint(p)?.score ?? 0);

	const hexLayer = L.hexbinLayer({
		radius: 45,
		opacity: 0.78,
		duration: 180,
		colorRange: ["hsl(210,70%,45%)", "hsl(20,80%,45%)"],
		radiusRange: [43, 43],
		pointerEvents: "all",
	})
		.lng((d) => d.lng)
		.lat((d) => d.lat)
		.colorValue((bin) => binScore(bin))
		.radiusValue(() => 1)
		.fill((bin) => colorFor(binScore(bin)))
		.hoverHandler(L.HexbinHoverHandler.tooltip({
			tooltipContent: (bin) => {
				const n = bin.length;
				const sum = binScore(bin);
				return `${n} Ort${n === 1 ? "" : "e"} · ${sum} Ereignisse`;
			},
		}));

	hexLayer.addTo(map);
	hexLayer.data(points);

	const markSinglePlaceHexagons = () => {
		requestAnimationFrame(() => {
			d3.select(map.getPanes().overlayPane)
				.selectAll("g.hexbin-container")
				.classed("hexbin-single-place", (bin) => Array.isArray(bin) && bin.length === 1);
		});
	};
	markSinglePlaceHexagons();
	map.on("moveend", markSinglePlaceHexagons);

	hexLayer.dispatch().on("click", function (bin) {
		if (typeof d3 !== "undefined" && d3.event?.stopPropagation) {
			d3.event.stopPropagation();
		}

		if (!Array.isArray(bin) || !bin.length) return;
		const entries = bin.map((p) => unwrapPoint(p)).filter(Boolean);
		if (!entries.length) return;

		if (entries.length === 1) {
			const feature = entries[0].feature;
			if (!feature) return;
			sidebar.replaceChildren(buildSidebarContent(feature.properties ?? {}, feature.id));
			setLocationIdInUrl(feature.id);
			return;
		}

		sidebar.replaceChildren(buildHexbinSidebarContent(entries));
		setLocationIdInUrl(null);
	});

	map.on("click", () => {
		setLocationIdInUrl(null);
		sidebar.replaceChildren(sidebarHintHtml());
	});

	if (points.length) {
		const bounds = L.latLngBounds(points.map((p) => [p.lat, p.lng]));
		map.fitBounds(bounds, { padding: [30, 30] });
	} else {
		map.setView([20, 0], 2);
	}

	// Pre-select location from URL parameter.
	const urlId = getLocationIdFromUrl();
	if (urlId) {
		const point = byId[urlId];
		if (point) {
			sidebar.replaceChildren(buildSidebarContent(point.feature.properties ?? {}, point.feature.id));
			map.setView([point.lat, point.lng], Math.max(map.getZoom(), LABEL_MIN_ZOOM));
		}
	}
});
