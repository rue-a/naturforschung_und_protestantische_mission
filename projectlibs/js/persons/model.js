/* =====================================================
   model.js  —  load persons.json, filtering, URL helpers
   ===================================================== */

/**
 * Fetch persons.json and return a Map keyed by person id,
 * sorted alphabetically by preferred name.
 * @param {string} url
 * @returns {Promise<Map<string, object>>}
 */
async function loadPersons(url) {
	const response = await fetch(url);
	if (!response.ok) throw new Error(`Failed to load persons: ${response.status}`);
	const persons = await response.json();

	const sorted = persons.sort((a, b) => {
		const na = a.name?.surname?.label ?? a.name?.preferred?.label ?? "";
		const nb = b.name?.surname?.label ?? b.name?.preferred?.label ?? "";
		return na.localeCompare(nb, "de");
	});

	return new Map(sorted.map(p => [p.id, p]));
}

/**
 * Filter a persons Map by a free-text query against the preferred name.
 * Returns all persons as an ordered array when the query is empty.
 * @param {Map<string, object>} personsMap
 * @param {string} query
 * @returns {object[]}
 */
function filterPersons(personsMap, query) {
	const q = query.trim().toLowerCase();
	const visible = Array.from(personsMap.values()).filter(p => p.visible);
	if (!q) return visible;
	return visible.filter(p => (p.name?.preferred?.label ?? "").toLowerCase().includes(q));
}

/**
 * Read the ?personid= query parameter from the current URL.
 * @returns {string|null}
 */
function getPersonIdFromUrl() {
	return new URLSearchParams(window.location.search).get("personid");
}

/**
 * Write ?personid=<id> into the URL without triggering a page reload.
 * @param {string} id
 */
function setPersonIdInUrl(id) {
	const url = new URL(window.location.href);
	url.searchParams.set("personid", id);
	history.pushState(null, "", url.toString());
}
