let btn=document.getElementById('login-btn')
let cookie=getCookie('login_staus')
let logout_url=document.getElementById('logout_url').textContent
let login_url=document.getElementById('login_url').textContent
if (cookie===true){
  btn.textContent='Выход'
  btn.href=logout_url
}
else {
  btn.textContent='Вход'
  btn.href=login_url
}
