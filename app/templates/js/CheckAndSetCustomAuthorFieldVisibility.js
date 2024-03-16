import { settings } from "./settings.js";

class CheckAndSetCustomAuthorFieldVisibility {
  constructor() {
  this.getElements();
  this.initActions();
  }
  
  getElements = () => {
    this.dom = {
      authorSelect: document.getElementById(settings.selectors.authorSelect),
      customAuthorField: document.querySelector(settings.selectors.customAuthor),
    }
  }
  
  initActions = () => {
    if (this.dom.authorSelect && this.dom.customAuthorField) {
      this.checkAndSetCustomAuthorFieldVisibility();
    this.dom.authorSelect.addEventListener('change', () => {
      this.checkAndSetCustomAuthorFieldVisibility();
    });
    }
  }

  checkAndSetCustomAuthorFieldVisibility = () => {
    const authorOptions = this.dom.authorSelect.querySelectorAll(settings.selectors.authorOptions);
    let customOptionSelected = false;
    for (let singleOption of authorOptions) {
      if (singleOption.value === 'custom' && singleOption.selected) {
        customOptionSelected = true;
        break;
      }
    }
    if (customOptionSelected) {
      this.dom.customAuthorField.style.display = settings.styles.block;
    } else {
      this.dom.customAuthorField.style.display = settings.styles.none;
    }
  };
}
  
export default CheckAndSetCustomAuthorFieldVisibility;