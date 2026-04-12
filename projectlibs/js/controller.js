window.AppController = (() => {
  const { state } = window.AppModel;
  const { DOM } = window.AppView;

  async function initializeApp() {
    await window.AppModel.loadData();
    window.AppView.setupMap();
    bindEvents();
    window.AppView.renderBrowser();
    window.AppView.showApp();

    const firstPersonButton = DOM.browser.querySelector("button");
    if (firstPersonButton) {
      firstPersonButton.click();
      return;
    }

    renderApp();
  }

  function bindEvents() {
    DOM.searchInput.addEventListener("input", handleSearch);
    DOM.mapTimeSlider.addEventListener("input", handleMapTimeInput);
  }

  function handleSearch(event) {
    const query = event.target.value.trim().toLowerCase();

    state.filteredPersonIds = Object.keys(state.personsById)
      .sort((a, b) => {
        const leftSurname = state.personsById[a].name.surname.value.value;
        const rightSurname = state.personsById[b].name.surname.value.value;
        return leftSurname.localeCompare(rightSurname, "de");
      })
      .filter((personId) => {
      const record = state.personsById[personId];
      const haystack = [
        personId,
        record.name.preferred.value.value,
        "surname" in record.name ? record.name.surname.value.value : "",
        "given_name" in record.name ? record.name.given_name.value.value : "",
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return haystack.includes(query);
    });

    renderApp();
  }

  function selectPerson(personId) {
    state.selectedPersonId = personId;
    state.mapTimeYear = null;
    renderApp();
  }

  function handleMapTimeInput(event) {
    state.mapTimeYear = Number(event.target.value);
    window.AppView.renderSelectedPerson();
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
