/* =====================================================
   model.js  —  domain logic for locations data
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

/**
 * Read the ?locationid= query parameter from the current URL.
 * @returns {string|null}
 */
function getLocationIdFromUrl() {
	return new URLSearchParams(window.location.search).get("locationid");
}

/**
 * Write ?locationid=<id> into the URL without triggering a page reload.
 * @param {string|null} id  — pass null to remove the parameter
 */
function setLocationIdInUrl(id) {
	const url = new URL(window.location.href);
	if (id == null) {
		url.searchParams.delete("locationid");
	} else {
		url.searchParams.set("locationid", id);
	}
	history.pushState(null, "", url.toString());
}

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


