import datetime

from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class News(models.Model):
  title = models.CharField(max_length=200)
  main_text = RichTextUploadingField(null=True, blank=False)
  preview = models.CharField(max_length=150)
  public_date = models.DateField(default=timezone.now())
  image = models.ImageField(upload_to='files/', blank=True, null=True)
  tags = models.CharField(max_length=20, default='cold')

  def get_absolute_url(self):
    return reverse('news_detail', kwargs={'_id': self.id})

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'


def upload_news(title, main_text, preview, public_date, image):
  record = News(title, main_text, preview, public_date, image)
  record.save()
