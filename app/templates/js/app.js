import { settings } from "./settings.js";
import CheckAndSetCustomFieldVisibility from "./CheckAndSetCustomFieldVisibility.js";

export const app = {
  init: function() {
    this.checkAuthorField = new CheckAndSetCustomFieldVisibility(
      settings.selectors.author,
      settings.selectors.customAuthor,
    );
    this.checkBorrowerField = new CheckAndSetCustomFieldVisibility(
      settings.selectors.borrower,
      settings.selectors.customBorrower,
    );
  }
}

app.init();
