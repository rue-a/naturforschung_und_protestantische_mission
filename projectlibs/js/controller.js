window.AppController = (() => {
  const {
    state,
    getFieldValue,
    getPersonSortName,
    getRoutePersonId,
    updateSelectedPersonUrl,
  } = window.AppModel;
  const { DOM } = window.AppView;

  async function initializeApp() {
    await window.AppModel.loadData();
    window.AppView.setupMap();
    bindEvents();
    window.AppView.renderBrowser();
    window.AppView.showApp();

    const initialPersonId = getRoutePersonId() || state.filteredPersonIds[0];
    if (initialPersonId) {
      selectPerson(initialPersonId, { replaceUrl: true });
    } else {
      renderApp();
    }
  }

  function bindEvents() {
    DOM.searchInput.addEventListener("input", handleSearch);
    DOM.mapTimeSlider.addEventListener("input", handleMapTimeInput);
    window.addEventListener("popstate", handlePopState);
  }

  function handleSearch(event) {
    const query = event.target.value.trim().toLowerCase();

    state.filteredPersonIds = Object.keys(state.personsById)
      .sort((a, b) => {
        return getPersonSortName(state.personsById[a]).localeCompare(
          getPersonSortName(state.personsById[b]),
          "de"
        );
      })
      .filter((personId) => {
      const record = state.personsById[personId];
      const haystack = [
        personId,
        getFieldValue(record.name.preferred),
        "surname" in record.name ? getFieldValue(record.name.surname) : "",
        "given_name" in record.name ? getFieldValue(record.name.given_name) : "",
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return haystack.includes(query);
    });

    renderApp();
  }

  function selectPerson(personId, { updateUrl = true, replaceUrl = false } = {}) {
    state.selectedPersonId = personId;
    state.mapTimeYear = null;

    if (updateUrl) {
      updateSelectedPersonUrl(personId, { replace: replaceUrl });
    }

    renderApp();
  }

  function handleMapTimeInput(event) {
    state.mapTimeYear = Number(event.target.value);
    window.AppView.renderSelectedPerson();
  }

  function handlePopState() {
    const routePersonId = getRoutePersonId();

    if (routePersonId) {
      selectPerson(routePersonId, { updateUrl: false });
      return;
    }

    if (state.filteredPersonIds[0]) {
      selectPerson(state.filteredPersonIds[0], { replaceUrl: true });
      return;
    }

    state.selectedPersonId = null;
    renderApp();
  }

  function renderApp() {
    window.AppView.renderBrowser();
    window.AppView.renderSelectedPerson();
  }

  document.addEventListener("DOMContentLoaded", () => {
    initializeApp();
  });

  return {
    initializeApp,
    selectPerson,
  };
})();
