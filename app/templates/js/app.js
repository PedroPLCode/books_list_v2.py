import CheckAndSetCustomAuthorFieldVisibility from "./CheckAndSetCustomAuthorFieldVisibility.js";

export const app = {
  init: function() {
    this.checkAndSetCustomAuthorFieldVisibility = new CheckAndSetCustomAuthorFieldVisibility();
  }
}

app.init();
