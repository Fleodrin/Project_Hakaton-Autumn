import {popup} from "./popup.js";

const popupProvost = document.querySelector('.popup-provost');
const buttonProvost = document.querySelector('.popup-provost__button');
const feedback = document.getElementById('feedback');

if (feedback.textContent === '2') {
  popup(popupProvost, buttonProvost);
}
