from django.shortcuts import render, redirect

# Create your views here.
from user.models import User
from user.models import add_user


def register(request):
  name = request.POST.get('field-name')
  email = request.POST.get('field-email')
  error = 0
  try:
    user = User.objects.get(email=email)
    error = 1
  except User.DoesNotExist:
    user = None
  password = request.POST.get('field-pass')
  who = request.POST.get('product-group')
  if request.method == 'POST' and name is not None and user is None:
    add_user(name, email, password, who)
    return redirect('general')
  return render(request, 'register.html', context={'error': error})


def login(request):
  email_form = request.POST.get('field-email')
  user = None
  tmp = 0
  if email_form is not None:
    try:
      user = User.objects.get(email=email_form)
    except User.DoesNotExist:
      user = None
  if user is not None:
    password_form = request.POST.get('field-pass')
    if password_form == user.password:
      tmp = 1
    else:
      tmp = 2
  context = {
    'action': tmp
  }
  if tmp == 1:
    obj = redirect('general')
    obj.set_cookie('login_status', True, 60 * 60 * 24 * 15)
    return obj
  else:
    return render(request, 'login.html', context)


def logout(request):
  final = redirect('general')
  final.set_cookie('login_status', True, -1)
  return final
