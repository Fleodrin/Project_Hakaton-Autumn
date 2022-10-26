from django.db import models
from django.urls import reverse


class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=30)
  password = models.CharField(max_length=40)
  who = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_email(self):
    return self.email

  def get_password(self):
    return self.password

  def get_absolute_url(self):
    return reverse('user', args=[str(self.id)])


def add_user(name, email, password, who):
  record = User(name=name, email=email, password=password, who=who)
  record.save()
