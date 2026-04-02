# Frontend JS

The frontend is split into three files:

- `model.js`: loads data and stores shared state
- `view.js`: renders HTML and the map
- `controller.js`: reacts to user input and updates the app

The files communicate through global objects on `window`:

- `window.AppModel`
- `window.AppView`
- `window.AppController`

Example:

```js
window.AppController = (() => {
  function selectPerson(personId) {
    // ...
  }

  return { selectPerson };
})();
```

This means:

1. the function runs immediately
2. it returns an object
3. that object is stored on `window.AppController`

So other files can call `window.AppController.selectPerson(...)` without imports or a build step.
