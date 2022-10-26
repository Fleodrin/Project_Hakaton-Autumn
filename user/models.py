from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone


class UserManager(BaseUserManager):
  def _create_user(self, email, password, **extra_fields):
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('The given email must be set')
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=30, unique=True)
  password = models.CharField(max_length=200)
  who = models.CharField(max_length=20)
  date_register = models.DateTimeField(default=timezone.now)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  USERNAME_FIELD = 'email'
  objects = UserManager()

  def __str__(self):
    return self.name

  def get_email(self):
    return self.email

  def get_password(self):
    return self.password

  def get_absolute_url(self):
    return reverse('user', args=[str(self.id)])

  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


def add_user(name, email, password, who):
  record = User(name=name, email=email, password=password, who=who)
  record.save()
