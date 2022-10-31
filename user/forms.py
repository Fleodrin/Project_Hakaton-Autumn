from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from user.models import User


class LoginForm(forms.Form):
  email = forms.CharField(widget=forms.TextInput())
  password = forms.CharField(
    widget=forms.PasswordInput(),
  )


class RegistrationForm(UserCreationForm):
  name = forms.CharField(widget=forms.TextInput())
  email = forms.CharField(widget=forms.TextInput())

  class Meta:

    model = User
    fields = ('name', 'email', 'productgroup','is_staff')

  def save(self, commit=True):

    user = super().save(commit=False)
    print(user)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user

  def __init__(self, *args, **kwargs):
    super(RegistrationForm, self).__init__(*args, **kwargs)
    if self.data['productgroup'] == 'professor':
      self.initial['is_staff'] = True
    else:
      self.initial['is_staff'] = False
