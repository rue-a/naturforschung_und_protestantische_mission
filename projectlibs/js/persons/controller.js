/* =====================================================
   controller.js  —  wires model, view, and map together
   ===================================================== */

// Path relative to html/persons.html
const PERSONS_DATA_URL = "../data/persons.json";

let _persons = new Map();
let _selectedId = null;

/**
 * Select a person: update the metadata panel, content area, map, URL,
 * and the highlighted item in the list.
 * @param {string} id
 */
function selectPerson(id) {
	_selectedId = id;
	setPersonIdInUrl(id);

	const person = _persons.get(id);
	if (!person) return;

	renderMetaPanel(person);
	renderContentArea(person);
	renderTrajectory(person.life_trajectory);

	// Update highlight in the list
	document.querySelectorAll("#person-list li").forEach(li => {
		li.classList.toggle("selected", li.dataset.id === id);
	});

	// Scroll selected item into view without affecting the page scroll
	document.querySelector(`#person-list li[data-id="${id}"]`)
		?.scrollIntoView({ block: "nearest" });
}

/**
 * Apply a search query and re-render the list, preserving the current selection.
 * @param {string} query
 */
function applyFilter(query) {
	renderList(filterPersons(_persons, query), _selectedId, selectPerson);
}

// ─── Initialisation ───────────────────────────────────────────────────────────

document.addEventListener("DOMContentLoaded", async () => {
	_persons = await loadPersons(PERSONS_DATA_URL);

	// Initial list (all persons, already sorted by loadPersons)
	renderList(Array.from(_persons.values()), null, selectPerson);

	// Pre-select person from URL parameter
	const urlId = getPersonIdFromUrl();
	if (urlId && _persons.has(urlId)) {
		selectPerson(urlId);
	}

	// Search with 200 ms debounce
	let debounceTimer;
	document.getElementById("person-search").addEventListener("input", e => {
		clearTimeout(debounceTimer);
		debounceTimer = setTimeout(() => applyFilter(e.target.value), 200);
	});
});
