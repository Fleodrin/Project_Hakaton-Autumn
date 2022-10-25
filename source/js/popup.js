const popupLogin = document.querySelector('.popup-login');
const login = document.getElementById('loginResult');
const bruh=document.getElementById('bruh')
const popupProvost = document.querySelector('.popup-provost');
const buttonProvost = document.querySelector('.popup-provost__button');
const feedback = document.getElementById('feedback');
const popup = (popupName, buttonName) => {
  popupName.classList.remove('popup--close');
  buttonName.onclick = () => {
    return popupName.classList.add('popup--close');
  };

  window.setTimeout(addHidden, 5000);

  function addHidden() {
    return popupName.classList.add('popup--close');
  }
}

if (login.textContent === '1') {
  popup(popupLogin);
}

if (feedback.textContent === '2') {
  popup(popupProvost, buttonProvost);
}
bruh.textContent=a;
