/* =====================================================
   controller.js  —  wire model and map for the locations page
   ===================================================== */

// Path relative to htm/locations.html
const LOCATIONS_DATA_URL = "../data/locations.json";

document.addEventListener("DOMContentLoaded", async () => {
	const featureCollection = await loadLocations(LOCATIONS_DATA_URL);
	renderLocationsMap(featureCollection);
});
