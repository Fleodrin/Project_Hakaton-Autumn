from django.contrib import admin
from django import forms
from .models import News
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

class NewsAdminForm(forms.ModelForm):
  main_text = forms.CharField(widget=CKEditorUploadingWidget())

  class Meta:
    model = News
    fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
  list_display = '__all__'
  form = NewsAdminForm
