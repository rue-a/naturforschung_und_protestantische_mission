/* =====================================================
   model.js  —  load the locations JSON-FG FeatureCollection
   ===================================================== */

/**
 * Fetch and return the locations FeatureCollection.
 * @param {string} url
 * @returns {Promise<object>}  JSON-FG FeatureCollection
 */
async function loadLocations(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`Failed to load locations: ${response.status}`);
	return response.json();
}
