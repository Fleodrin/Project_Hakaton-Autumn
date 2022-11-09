from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from news.models import News


class NewsCreateForm(forms.ModelForm):
  class Meta:
    choise = [('hot', 'Горячие'), ('cold', 'Холодные')]
    model = News
    fields = ['title', 'preview', 'tags', 'main_text', 'image']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'news-create-form-title'}),
      'main_text': CKEditorUploadingWidget(attrs={'class': 'news-create-form-main-text'}),
      'preview': forms.TextInput(attrs={'class': 'news-create-form-preview'}),
      'image': forms.FileInput(attrs={'class': 'news-create-form-image'}),
      'tags': forms.Select(attrs={'class': 'news-create-form-tags'}, choices=choise),
    }
