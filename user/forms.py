from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class LoginForm(forms.Form):
  email = forms.CharField(widget=forms.TextInput())
  password = forms.CharField(
    widget=forms.PasswordInput(),
  )


class RegistrationForm(UserCreationForm):
  name = forms.CharField(widget=forms.TextInput())
  email = forms.CharField(widget=forms.TextInput())

  # field_password = forms.CharField(
  #   widget=forms.PasswordInput(),
  # )
  # field_pass_repeat = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ('name', 'email')

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user
