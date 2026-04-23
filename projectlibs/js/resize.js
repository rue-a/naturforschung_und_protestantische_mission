/* =====================================================
   resize.js  —  drag-to-resize panel handles
   Handles:
	 .col-resize-handle  → resizes .right-panel width
	 .row-resize-handle  → resizes .meta-panel / #trajectory-map split
   ===================================================== */

(function () {
	"use strict";

	function initResize() {
		const layout = document.querySelector(".persons-layout");
		const hHandle = document.querySelector(".col-resize-handle");
		const rightPanel = document.querySelector(".right-panel");
		const vHandle = document.querySelector(".row-resize-handle");
		const metaPanel = document.querySelector(".meta-panel");
		const mapEl = document.querySelector("#trajectory-map");

		// ------------------------------------------------------------------
		// Horizontal: drag .col-resize-handle to change right panel width
		// ------------------------------------------------------------------
		if (hHandle && rightPanel && layout) {
			hHandle.addEventListener("mousedown", (e) => {
				e.preventDefault();
				const startX = e.clientX;
				const startW = rightPanel.getBoundingClientRect().width;
				const layoutW = layout.getBoundingClientRect().width;

				hHandle.classList.add("dragging");
				document.body.classList.add("resizing");

				const onMove = (e) => {
					const delta = startX - e.clientX;
					const newW = Math.max(180, Math.min(layoutW * 0.72, startW + delta));
					rightPanel.style.width = newW + "px";
				};

				const onUp = () => {
					hHandle.classList.remove("dragging");
					document.body.classList.remove("resizing");
					document.removeEventListener("mousemove", onMove);
					document.removeEventListener("mouseup", onUp);
					if (typeof _trajectoryMap !== "undefined" && _trajectoryMap) {
						_trajectoryMap.invalidateSize();
					}
				};

				document.addEventListener("mousemove", onMove);
				document.addEventListener("mouseup", onUp);
			});
		}

		// ------------------------------------------------------------------
		// Vertical: drag .row-resize-handle to split meta panel / map
		// ------------------------------------------------------------------
		if (vHandle && metaPanel && mapEl) {
			vHandle.addEventListener("mousedown", (e) => {
				e.preventDefault();
				const startY = e.clientY;
				const startMetaH = metaPanel.getBoundingClientRect().height;
				const startMapH = mapEl.getBoundingClientRect().height;

				vHandle.classList.add("dragging");
				document.body.classList.add("resizing-v");

				const onMove = (e) => {
					const delta = e.clientY - startY;
					const newMetaH = Math.max(80, startMetaH + delta);
					const newMapH = Math.max(80, startMapH - delta);
					metaPanel.style.flex = "none";
					metaPanel.style.height = newMetaH + "px";
					mapEl.style.height = newMapH + "px";
				};

				const onUp = () => {
					vHandle.classList.remove("dragging");
					document.body.classList.remove("resizing-v");
					document.removeEventListener("mousemove", onMove);
					document.removeEventListener("mouseup", onUp);
					if (typeof _trajectoryMap !== "undefined" && _trajectoryMap) {
						_trajectoryMap.invalidateSize();
					}
				};

				document.addEventListener("mousemove", onMove);
				document.addEventListener("mouseup", onUp);
			});
		}
	}

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", initResize);
	} else {
		initResize();
	}
})();
