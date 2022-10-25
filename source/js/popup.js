const popup = (popupName, buttonName) => {
  popupName.classList.remove('popup--close');

  if (buttonName) {
    buttonName.onclick = () => {
      return popupName.classList.add('popup--close');
    };
  }


  window.setTimeout(addHidden, 5000);
  function addHidden() {
    return popupName.classList.add('popup--close');
  }
}

export {popup};
