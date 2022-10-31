from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user.models import User
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
        request.session['logined'] = True
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
    return render(request, self.template, context={'form': self.form})

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST.copy())

    if form.is_valid():
      user = form.save(commit=False)
      if user.productgroup == 'professor':
        user.is_staff = True
        user.is_user = False
        user.groups = 'staff'
      elif user.productgroup == 'student':
        user.is_student = True
        user.is_user = False
      user.save()
      login(request, user, 'user.backend.UserBackend')
      request.session['logined'] = True
      return redirect('general')
    else:
      print(form.errors)
      return render(request, self.template, {'form': form})


def logout(request):
  logout_dj(request)
  return redirect('general')
