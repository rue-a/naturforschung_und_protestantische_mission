index.html                              ← landing page
serve.sh                                ← bash serve.sh → http://localhost:8080
css/base.css                            ← tokens, reset, header, footer
css/persons.css                         ← 3-col grid, panels, table, badges
css/locations.css                       ← full-viewport flex layout
htm/persons.html                        ← 3-col layout + trajectory map
htm/locations.html                      ← full-viewport map
projectlibs/js/persons/model.js         ← load, filter, URL helpers
projectlibs/js/persons/view.js          ← list + meta panel + content area
projectlibs/js/persons/map.js           ← Leaflet trajectory (birth/death/POE)
projectlibs/js/persons/controller.js   ← wires everything, ?personid=, debounce
projectlibs/js/locations/model.js       ← fetch FeatureCollection
projectlibs/js/locations/map.js         ← Leaflet circle markers + tooltips
projectlibs/js/locations/controller.js ← fetch + render