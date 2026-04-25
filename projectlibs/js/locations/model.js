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

/**
 * Marker style based on a normalised importance value t ∈ [0, 1].
 * Radius scales with √t from 4 to 14 px.
 * Hue interpolates from 210° (blue) → 20° (orange-red) as importance rises.
 * Zero-importance locations are rendered in a neutral grey.
 * @param {number} score
 * @param {number} maxScore
 * @returns {{ radius: number, fillColor: string, color: string, labelColor: string }}
 */
function _markerStyle(score, maxScore) {
	if (score === 0 || maxScore === 0) {
		return {
			radius: 4,
			fillColor: "hsl(0,0%,65%)",
			color: "hsl(0,0%,40%)",
			labelColor: "hsl(0,0%,22%)",
		};
	}
	const t = Math.sqrt(score / maxScore);
	const radius = 4 + t * 10;
	const hue = Math.round(210 - t * 190); // 210 (blue) → 20 (orange-red)
	return {
		radius,
		fillColor: `hsl(${hue},70%,45%)`,
		color: `hsl(${hue},70%,28%)`,
		labelColor: `hsl(${hue},80%,20%)`,
	};
}
