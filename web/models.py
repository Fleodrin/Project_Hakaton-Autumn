from django.db import models

# Create your models here.
from django.urls import reverse


class Feedback(models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(max_length=100, null=True)
  text = models.CharField(max_length=1000)

  def __str__(self):
    return self.email

  class Meta:
    verbose_name = 'Фидбэк'
    verbose_name_plural = 'Фидбэки'


def add_feedback(name, email, text):
  record = Feedback(name=name, email=email, text=text)
  record.save()
