import json
import sys
from django.core import serializers
from django.contrib.sessions.backends.cached_db import SessionStore
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url

from news.models import News
from webapp import urls
from .models import add_feedback
import logging, logging.config
import sys


def index(request):
  context = {}
  if 'logined' in request.session:
    context.update({'login_feedback': 'true'})
    del request.session['logined']
  name = request.POST.get('feedback-name')
  email = request.POST.get('feedback-mail')
  message = request.POST.get('feedback-message')
  context_news = get_news_context(request)
  context.update(context_news)
  if request.method == 'POST' and name is not None:
    add_feedback(name, email, message)
    message = 'От: ' + name + '\n' + message + '\n' + 'Почта для связи: ' + email
    send_mail(subject='От: ' + name, message=message,
              from_email='rector.site@gmail.com',
              recipient_list=['rector.site@gmail.com'])
    res = {'result': '2'}
    context.update(res)

  return render(request, 'index.html', context)


def get_news_context(request):
  news = News.objects.all().order_by('-public_date')
  p = Paginator(news, 3)
  page = request.GET.get('page')
  newss = p.get_page(page)
  context_news = {
    'news': news,
  }
  print(News.objects.all())
  return context_news





def calendar(request):
  return 0


def events(request):
  return 0
