window.AppController = (() => {
  const { state } = window.AppModel;
  const { DOM } = window.AppView;

  async function initializeApp() {
    await window.AppModel.loadData();
    window.AppView.setupMap();
    bindEvents();
    renderApp();
    window.AppView.showApp();
  }

  function bindEvents() {
    DOM.searchInput.addEventListener("input", handleSearch);
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

    if (
      !state.filteredPersonIds.includes(state.selectedPersonId)
    ) {
      state.selectedPersonId =
        state.filteredPersonIds.length > 0 ? state.filteredPersonIds[0] : null;
    }

    renderApp();
  }

  function selectPerson(personId) {
    state.selectedPersonId = personId;
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
