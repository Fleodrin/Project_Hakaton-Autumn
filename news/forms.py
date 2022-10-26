from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from news.models import News


class NewsCreateForm(forms.ModelForm):

  class Meta:
    model = News
    fields = ['title', 'preview', 'main_text', 'image']
