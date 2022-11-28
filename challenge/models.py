from django.db import models


# Create your models here.
from django.urls import reverse


class Participant(models.Model):
  name = models.CharField(max_length=20)
  ligma = models.IntegerField()
  balls = models.IntegerField()

  def get_absolute_url(self):
    return reverse('news_detail', kwargs={'_id': self.id})

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Участник'
    verbose_name_plural = 'Участники'
