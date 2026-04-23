/* =====================================================
   view.js  —  render person list, metadata panel, content area
   ===================================================== */

// Asset base path, relative to html/persons.html
const ASSETS = "../assets";

// External link logos: key matches persons.json links object
const LINK_ASSETS = {
	wikidata: { file: "wikidata_18x12.svg", label: "Wikidata" },
	gnd: { file: "gnd.png", label: "GND" },
	factgrid: { file: "factgrid.png", label: "FactGrid" },
	bionomia: { file: "bionomia.png", label: "Bionomia" },
	saebi: { file: "saebi.png", label: "SäBI" },
};

// ─── Public render functions ─────────────────────────────────────────────────

/**
 * Populate #person-list with a (filtered) list of persons.
 * @param {object[]} persons    — ordered array of person objects
 * @param {string|null} selectedId
 * @param {function(string):void} onSelect  — called with person id on click
 */
function renderList(persons, selectedId, onSelect) {
	const ul = document.getElementById("person-list");
	ul.innerHTML = "";

	for (const person of persons) {
		const li = document.createElement("li");

		const nameSpan = document.createElement("span");
		nameSpan.className = "person-list-name";
		nameSpan.textContent = person.name?.preferred?.label ?? person.id;

		const idSpan = document.createElement("span");
		idSpan.className = "person-list-id";
		idSpan.textContent = person.id;

		li.append(nameSpan, idSpan);
		li.dataset.id = person.id;
		if (person.id === selectedId) li.classList.add("selected");
		li.addEventListener("click", () => onSelect(person.id));
		ul.appendChild(li);
	}
}

/**
 * Render the right-hand metadata panel for a person.
 * @param {object} person
 */
function renderMetaPanel(person) {
	const panel = document.getElementById("meta-panel");
	panel.innerHTML = "";

	const stickyHeader = document.createElement("h2");
	stickyHeader.className = "panel-sticky-header";
	const preferredName = person.name?.preferred?.label ?? person.id;
	stickyHeader.textContent = `Metadaten (${preferredName})`;
	panel.appendChild(stickyHeader);

	const body = document.createElement("div");
	body.className = "panel-body";
	body.appendChild(_buildBirthDeathSection(person));
	body.appendChild(_buildPoESection(person));
	body.appendChild(_buildMoraviansSection(person));
	body.appendChild(_buildBotanicalInfluenceSection(person));
	body.appendChild(_buildRelativesSection(person));
	body.appendChild(_buildContactSection(person));
	body.appendChild(_buildLinksSection(person));
	panel.appendChild(body);
}

/**
 * Render the middle content area (collections, works, citations) for a person.
 * @param {object} person
 */
function renderContentArea(person) {
	const area = document.getElementById("content-area");
	area.innerHTML = "";

	const stickyHeader = document.createElement("h1");
	stickyHeader.className = "panel-sticky-header";
	stickyHeader.textContent = person.name?.preferred?.label ?? person.id;
	area.appendChild(stickyHeader);

	const body = document.createElement("div");
	body.className = "panel-body";
	body.appendChild(_buildCollectionsSection(person));
	body.appendChild(_buildBotanicalWorksSection(person));
	body.appendChild(_buildBotanicalCitationsSection(person));
	body.appendChild(_buildWorksSection(person));
	body.appendChild(_buildCitationsSection(person));
	area.appendChild(body);
}

// ─── Metadata panel builders ─────────────────────────────────────────────────

function _buildNameSection(person) {
	const sec = _metaSection();
	const nameEl = document.createElement("div");
	nameEl.className = "meta-name";
	nameEl.textContent = person.name?.preferred?.label ?? person.id;
	sec.appendChild(nameEl);
	if (!person.visible) {
		const tag = document.createElement("span");
		tag.className = "meta-label";
		tag.textContent = "nicht im Personenlexikon";
		sec.appendChild(tag);
	}
	return sec;
}

function _buildBotanicalInfluenceSection(person) {
	const sec = _metaSection("Einfluss auf botanische Forschung");

	const botWorks = person.botany?.works ?? {};
	const nWorks =
		(botWorks.manuscripts?.length ?? 0) +
		(botWorks.printed?.length ?? 0);

	const nCitations =
		person.botany?.citations?.in_botanical_works_by_others?.length ?? 0;

	const contrib = person.botany?.contribution_to_collections ?? {};
	const nSammlungen =
		(contrib.object_evidence?.length ?? 0) +
		(contrib.database_evidence?.length ?? 0) +
		(contrib.literature_evidence?.length ?? 0);

	const p = document.createElement("p");
	p.className = "meta-influence-text";
	p.innerHTML =
		`Verfasste <strong>${nWorks}</strong> botanische Werke, ` +
		`wurde in <strong>${nCitations}</strong> botanischen Werken zitiert ` +
		`und trug zu <strong>${nSammlungen}</strong> Sammlungen bei.`;
	sec.appendChild(p);
	return sec;
}

function _buildBirthDeathSection(person) {
	const sec = _metaSection("Geburt & Tod");
	const events = [
		{ label: "Geburt", event: person.birth },
		{ label: "Tod", event: person.death },
	];
	for (const { label, event } of events) {
		if (!event) continue;
		const row = document.createElement("div");
		row.style.marginBottom = "var(--space-xs)";

		const lbl = document.createElement("span");
		lbl.className = "meta-label";
		lbl.textContent = label + ": ";
		row.appendChild(lbl);

		if (event.date?.label) {
			row.appendChild(_sourcedText(event.date.label, event.date.source));
		}
		if (event.location?.label) {
			row.appendChild(document.createTextNode(" · "));
			row.appendChild(
				event.location.link
					? _locationLink(event.location.label, event.location.link, event.location.source)
					: _sourcedText(event.location.label, event.location.source)
			);
		}
		sec.appendChild(row);
	}
	return sec;
}

function _buildPoESection(person) {
	const poes = person.places_of_effect ?? [];
	const sec = _metaSection("Wirkungsorte");
	if (!poes.length) { sec.appendChild(_empty()); return sec; }

	const ul = document.createElement("ul");
	ul.className = "poe-list";
	for (const poe of poes) {
		const li = document.createElement("li");

		const parts = [];
		const hasTemporal = !!poe.temporal?.label;
		if (hasTemporal) {
			const timeSpan = document.createElement("span");
			timeSpan.className = "poe-temporal";
			timeSpan.textContent = poe.temporal.label;
			parts.push(timeSpan);
		}
		if (poe.location?.label) {
			parts.push(
				poe.location.link
					? _locationLink(poe.location.label, poe.location.link, poe.location.source)
					: _sourcedText(poe.location.label, poe.location.source)
			);
		}
		const role = [poe.institution?.label, poe.occupation?.label].filter(Boolean).join(" · ");
		if (role) {
			const roleSpan = document.createElement("span");
			roleSpan.textContent = role;
			parts.push(roleSpan);
		}

		const container = poe.source ? document.createElement("span") : li;
		if (poe.source) {
			container.className = "sourced";
			container.addEventListener("click", (e) => {
				e.stopPropagation();
				_showSourcePopup(e, poe.source);
			});
		}
		for (let i = 0; i < parts.length; i++) {
			const sep = (i === 1 && hasTemporal) ? ": " : " · ";
			if (i > 0) container.appendChild(document.createTextNode(sep));
			container.appendChild(parts[i]);
		}
		if (poe.source) li.appendChild(container);
		ul.appendChild(li);
	}
	sec.appendChild(ul);
	return sec;
}

function _buildMoraviansSection(person) {
	const items = person.member_of_moravians ?? [];
	const sec = _metaSection("Mitgliedschaft Brüdergemeine");
	if (!items.length) { sec.appendChild(_empty()); return sec; }

	const ul = document.createElement("ul");
	for (const m of items) {
		const li = document.createElement("li");
		li.appendChild(_sourcedText(m.label, m.source));
		ul.appendChild(li);
	}
	sec.appendChild(ul);
	return sec;
}

function _buildRelativesSection(person) {
	const rel = person.relatives ?? {};
	const sec = _metaSection("Verwandte");
	const groups = [
		["Geschwister", rel.siblings ?? []],
		["Ehepartner", rel.spouses ?? []],
		["Kinder", rel.children ?? []],
	];
	let hasContent = false;
	for (const [groupLabel, list] of groups) {
		if (!list.length) continue;
		hasContent = true;
		sec.appendChild(_groupLabel(groupLabel));
		sec.appendChild(_personList(list));
	}
	if (!hasContent) sec.appendChild(_empty());
	return sec;
}

function _buildContactSection(person) {
	const contact = person.contact ?? {};
	const sec = _metaSection("Kontakt");
	const groups = [
		["Mit Herrnhutern", contact.with_moravians ?? []],
		["Mit Nicht-Herrnhutern", contact.with_non_moravians ?? []],
	];
	let hasContent = false;
	for (const [groupLabel, list] of groups) {
		if (!list.length) continue;
		hasContent = true;
		sec.appendChild(_groupLabel(groupLabel));

		const ul = document.createElement("ul");
		for (const p of list) {
			const li = document.createElement("li");
			// temporal is not in current data but guard for future use
			const temporal = p.temporal?.label;
			const text = temporal ? `${p.label} (${temporal})` : p.label;
			li.appendChild(_sourcedText(text, p.source));
			li.appendChild(document.createTextNode(" "));
			if (p.link) li.appendChild(_wikidataIconLink(p.link));
			ul.appendChild(li);
		}
		sec.appendChild(ul);
	}
	if (!hasContent) sec.appendChild(_empty());
	return sec;
}

function _buildLinksSection(person) {
	const links = person.links ?? {};
	const sec = _metaSection("Links");
	const row = document.createElement("div");
	row.className = "person-links";

	for (const [key, meta] of Object.entries(LINK_ASSETS)) {
		const url = links[key]?.label;
		if (!url) continue;
		const a = document.createElement("a");
		a.href = url;
		a.target = "_blank";
		a.rel = "noopener noreferrer";
		a.title = meta.label;
		const img = document.createElement("img");
		img.src = `${ASSETS}/${meta.file}`;
		img.alt = meta.label;
		a.appendChild(img);
		row.appendChild(a);
	}

	if (!row.children.length) row.appendChild(_empty());
	sec.appendChild(row);
	return sec;
}

// ─── Content area builders ────────────────────────────────────────────────────

function _buildCollectionsSection(person) {
	const contrib = person.botany?.contribution_to_collections ?? {};
	const groups = [
		["Objektnachweis", "Der Beitrag zu den aufgeführten Sammlungen wird verifiziert durch ein nachweislich von der Person gesammeltes Objekt, welches Teil der entsprechenden Sammlung ist.", contrib.object_evidence ?? []],
		["Datenbanknachweis", "Der Beitrag zu den aufgeführten Sammlungen wird verifiziert durch eine Angabe über einen Beitrag zur entsprechenden in einer Sammlungsdatenbank.", contrib.database_evidence ?? []],
		["Literaturnachweis", "Der Beitrag zu den aufgeführten Sammlungen wird verifiziert durch eine Angabe über einen Beitrag zur entsprechenden in der Literatur.", contrib.literature_evidence ?? []],
	];
	const sec = _contentSection("Sammlungsbeiträge");
	const hasAny = groups.some(([, , list]) => list.length > 0);
	if (!hasAny) { sec.appendChild(_empty()); return sec; }

	for (const [groupLabel, tooltip, items] of groups) {
		if (!items.length) continue;
		const lbl = _groupLabel(groupLabel);
		const sup = document.createElement("sup");
		sup.className = "info-btn";
		sup.textContent = "?";
		sup.addEventListener("click", () => {
			const existing = lbl.querySelector(".info-tooltip");
			if (existing) { existing.remove(); return; }
			const tip = document.createElement("span");
			tip.className = "info-tooltip";
			tip.textContent = tooltip;
			lbl.appendChild(tip);
		});
		lbl.appendChild(sup);
		sec.appendChild(lbl);
		const ul = document.createElement("ul");
		ul.className = "works-list";
		for (const c of items) {
			const li = document.createElement("li");
			li.appendChild(_sourcedText(c.label, c.source));
			if (c.nybg_herbarium_code) {
				const code = document.createElement("span");
				code.className = "collection-nybg";
				code.textContent = ` (${c.nybg_herbarium_code})`;
				li.appendChild(code);
			}
			if (c.link) {
				const a = document.createElement("a");
				a.href = c.link;
				a.target = "_blank";
				a.rel = "noopener noreferrer";
				a.className = "collection-link";
				a.textContent = "\u2197";
				a.setAttribute("aria-label", "Webseite öffnen");
				li.appendChild(a);
			}
			ul.appendChild(li);
		}
		sec.appendChild(ul);
	}
	return sec;
}

function _buildBotanicalWorksSection(person) {
	const works = person.botany?.works ?? {};
	const manuscripts = works.manuscripts ?? [];
	const printed = works.printed ?? [];
	const sec = _contentSection("Botanische Werke");
	if (!manuscripts.length && !printed.length) { sec.appendChild(_empty()); return sec; }

	if (manuscripts.length) {
		sec.appendChild(_groupLabel("Manuskripte"));
		sec.appendChild(_workList(manuscripts));
	}
	if (printed.length) {
		sec.appendChild(_groupLabel("Druckwerke"));
		sec.appendChild(_workList(printed));
	}
	return sec;
}

function _buildBotanicalCitationsSection(person) {
	const items = person.botany?.citations?.in_botanical_works_by_others ?? [];
	const sec = _contentSection("Botanische Zitierungen");
	if (!items.length) { sec.appendChild(_empty()); return sec; }
	sec.appendChild(_workList(items));
	return sec;
}

function _buildWorksSection(person) {
	const items = person.works?.without_botanical_context ?? [];
	const sec = _contentSection("Werke (ohne botanischen Kontext)");
	if (!items.length) { sec.appendChild(_empty()); return sec; }
	sec.appendChild(_workList(items));
	return sec;
}

function _buildCitationsSection(person) {
	const items = person.citations?.in_non_botanical_works_by_others ?? [];
	const sec = _contentSection("Zitierungen (ohne botanischen Kontext)");
	if (!items.length) { sec.appendChild(_empty()); return sec; }
	sec.appendChild(_workList(items));
	return sec;
}

// ─── DOM helpers ──────────────────────────────────────────────────────────────

function _metaSection(title) {
	const div = document.createElement("div");
	div.className = "meta-section";
	if (title) {
		const h = document.createElement("h3");
		h.textContent = title;
		div.appendChild(h);
	}
	return div;
}

function _contentSection(title) {
	const div = document.createElement("div");
	div.className = "content-section";
	if (title) {
		const h = document.createElement("h3");
		h.textContent = title;
		div.appendChild(h);
	}
	return div;
}

function _empty() {
	const span = document.createElement("span");
	span.className = "placeholder-text";
	span.textContent = "—";
	return span;
}

function _groupLabel(text) {
	const div = document.createElement("div");
	div.className = "meta-label";
	div.style.marginBottom = "var(--space-xs)";
	div.textContent = text;
	return div;
}

/** Render a list of person refs, each optionally with a Wikidata icon. */
function _personList(items) {
	const ul = document.createElement("ul");
	for (const p of items) {
		const li = document.createElement("li");
		li.appendChild(_sourcedText(p.label, p.source));
		if (p.link) li.appendChild(_wikidataIconLink(p.link));
		ul.appendChild(li);
	}
	return ul;
}

/** Render a list of work/citation references with optional links. */
function _workList(items) {
	const ul = document.createElement("ul");
	ul.className = "works-list";
	for (const item of items) {
		const li = document.createElement("li");
		if (item.link) {
			const a = document.createElement("a");
			a.href = item.link;
			a.target = "_blank";
			a.rel = "noopener noreferrer";
			a.textContent = item.label;
			li.appendChild(a);
		} else {
			li.appendChild(_sourcedText(item.label, item.source));
		}
		ul.appendChild(li);
	}
	return ul;
}

/** Inline location text + Wikidata icon link. */
function _locationLink(label, href, source) {
	const wrap = document.createElement("span");
	wrap.appendChild(_sourcedText(label + " ", source));
	wrap.appendChild(_wikidataIconLink(href));
	return wrap;
}

/**
 * Wrap text in a dark-red clickable span that shows a source popup on click.
 * If no source is provided, returns a plain text node.
 */
function _sourcedText(text, source) {
	if (!source) return document.createTextNode(text);
	const span = document.createElement("span");
	span.className = "sourced";
	span.textContent = text;
	span.addEventListener("click", (e) => {
		e.stopPropagation();
		_showSourcePopup(e, source);
	});
	return span;
}

/** Render a fixed popup with source details near the click position. */
function _showSourcePopup(e, source) {
	document.querySelectorAll(".source-popup").forEach(p => p.remove());
	const popup = document.createElement("div");
	popup.className = "source-popup";

	const typeEl = document.createElement("div");
	typeEl.className = "source-popup-type";
	typeEl.textContent = source.type ? `Quelle (${source.type})` : "Quelle";
	popup.appendChild(typeEl);

	const labelText = source.label ?? "";
	// If the label itself looks like a URL, make it a link
	const labelEl = document.createElement("div");
	if (/^https?:\/\//i.test(labelText)) {
		const a = document.createElement("a");
		a.href = labelText;
		a.target = "_blank";
		a.rel = "noopener noreferrer";
		a.textContent = labelText;
		labelEl.appendChild(a);
	} else {
		labelEl.textContent = labelText;
	}
	popup.appendChild(labelEl);

	if (source.archive || source.signature) {
		const detailEl = document.createElement("div");
		detailEl.className = "source-popup-detail";
		const parts = [];
		if (source.archive) {
			const archiveStr = source.archive_abbreviation
				? `${source.archive} (${source.archive_abbreviation})`
				: source.archive;
			parts.push(archiveStr);
		}
		if (source.signature) parts.push(source.signature);
		detailEl.textContent = parts.join(": ");
		popup.appendChild(detailEl);
	}

	if (source.link) {
		const a = document.createElement("a");
		a.href = source.link;
		a.target = "_blank";
		a.rel = "noopener noreferrer";
		a.textContent = "↗ Quelle öffnen";
		popup.appendChild(a);
	}

	popup.style.top = (e.clientY + 10) + "px";
	popup.style.left = (e.clientX + 10) + "px";
	document.body.appendChild(popup);

	// Clamp to viewport
	requestAnimationFrame(() => {
		const r = popup.getBoundingClientRect();
		if (r.right > window.innerWidth - 10)
			popup.style.left = (window.innerWidth - r.width - 10) + "px";
		if (r.bottom > window.innerHeight - 10)
			popup.style.top = (e.clientY - r.height - 10) + "px";
	});

	// Close on outside click
	setTimeout(() => {
		const close = (ev) => {
			if (!popup.contains(ev.target)) {
				popup.remove();
				document.removeEventListener("click", close);
			}
		};
		document.addEventListener("click", close);
	}, 0);
}

/** Small Wikidata icon wrapped in an external link. */
function _wikidataIconLink(href) {
	const a = document.createElement("a");
	a.href = href;
	a.target = "_blank";
	a.rel = "noopener noreferrer";
	const img = document.createElement("img");
	img.src = `${ASSETS}/wikidata_18x12.svg`;
	img.alt = "Wikidata";
	img.className = "wikidata-icon";
	a.appendChild(img);
	return a;
}
