from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist


class UserBackend(BaseBackend):

  def get_user_model(func):
    user_model = get_user_model()

    def wrapper(self, *args, **kwargs):
      kwargs.setdefault('model', user_model)
      return func(self, *args, **kwargs)

    return wrapper

  @get_user_model
  def authenticate(self, request, **kwargs):
    email = kwargs.get('email') if kwargs.get('email') else kwargs.get('username')
    password = kwargs.get('password')
    try:
      user = kwargs.get('model').objects.get(email__iexact=email)
      pass_validator = user.check_password(password)
      if pass_validator:
        return user
    except ObjectDoesNotExist:
      return None

  @get_user_model
  def get_user(self, user_id, **kwargs):
    try:
      return kwargs.get('model').objects.get(pk=user_id)
    except:
      return None
