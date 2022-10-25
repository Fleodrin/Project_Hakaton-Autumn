from django.shortcuts import render

# Create your views here.
from news.models import News


def news(request):
  return render(request, 'test.html')


def news_detail(request, _id):
  instance = News.objects.get(id=_id)
  context = {
    'news': instance
  }
  return render(request, 'news_instance.html', context)
