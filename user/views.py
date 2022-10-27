from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user.models import User
from user.models import add_user
from django.views.generic import View, CreateView
from django.contrib.auth import login
from django.contrib.auth import logout as logout_dj
from .backend import UserBackend
from .forms import LoginForm, RegistrationForm


class LoginView(View):
  form = LoginForm
  template = 'login.html'

  def get(self, request, *args, **kwargs):
    return render(request, self.template)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    auth = UserBackend()
    if form.is_valid():
      user = auth.authenticate(request, **form.cleaned_data)
      if user:
        login(request, user, 'user.backend.UserBackend')
        return redirect('general')
      else:
        error = 'Пользователь не найден'
        return render(request, self.template, {'error': error})
    else:
      return render(request, self.template, {'form': form})


class RegistrationView(View):
  form = RegistrationForm
  template = 'register.html'

  def get(self, request, *args, **kwargs):
    return render(request, self.template)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    print(request.POST)
    print(form.is_valid())
    if form.is_valid():
      print(form.cleaned_data)
      user = form.save()
      login(request, user, 'user.backend.UserBackend')
      return redirect('general')
    else:
      print(form.errors)
      return render(request, self.template, {'form': form})


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


def logout(request):
  logout_dj(request)
  return redirect('general')
