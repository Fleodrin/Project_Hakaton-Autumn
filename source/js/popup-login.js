import {popup} from './popup.js'

const popupLogin = document.querySelector('.popup-login');
const login = document.getElementById('loginResult');


if (login.textContent === '1') {
  popup(popupLogin);
}
