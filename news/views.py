from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
# Create your views here.
from django.views import View

from news.models import News
from .forms import NewsCreateForm


def news(request):
  return render(request, 'test.html')


def news_detail(request, _id):
  instance = News.objects.get(id=_id)
  context = {
    'news': instance
  }
  return render(request, 'news_instance.html', context)


class NewsCreateView(View):
  template = 'news_create.html'
  form = NewsCreateForm

  def get(self, request, *args, **kwargs):
    if request.user.is_staff:
      return render(request, self.template, {'form': self.form})
    else:
      return redirect('general')

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('news')
    else:
      context = {'form': form}
      return render(request, self.template, context)
