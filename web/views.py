import sys

from django.contrib.sessions.backends.cached_db import SessionStore
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url

from webapp import urls
from .models import User, add_user, add_feedback, upload_news, News
import logging, logging.config
import sys


def index(request):
  context = {}
  try:
    cookie = request.COOKIES['login_status']
  except KeyError:
    cookie = None
  if cookie is not None:
    context.update({'login_status': cookie})
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
    res = {'result': 2}
    context.update(res)

  return render(request, 'index.html', context)


def get_news_context(request):
  news = News.objects.all().order_by('-public_date')
  p = Paginator(news, 3)
  page = request.GET.get('page')
  newss = p.get_page(page)
  context_news = {
    'news': newss,
  }
  return context_news


def register(request):
  name = request.POST.get('field-name')
  email = request.POST.get('field-email')
  error = 0
  try:
    user = User.objects.get(email=email)
    error = 1
  except User.DoesNotExist:
    user = None
  password = request.POST.get('field-pass')
  who = request.POST.get('product-group')
  if request.method == 'POST' and name is not None and user is None:
    add_user(name, email, password, who)
  return render(request, 'register.html', context={'error': error})


def login(request):
  email_form = request.POST.get('field-email')
  user = None
  tmp = 0
  if email_form is not None:
    try:
      user = User.objects.get(email=email_form)
    except User.DoesNotExist:
      user = None
  if user is not None:
    password_form = request.POST.get('field-pass')
    if password_form == user.password:
      tmp = 1
    else:
      tmp = 2
  context = {
    'action': tmp
  }
  if tmp == 1:
    context.update(get_news_context(request))
    obj = redirect('general')
    obj.set_cookie('login_status', True, 60 * 60 * 24 * 15)
    return obj
  else:
    return render(request, 'login.html', context)


def news(request):
  return 0


def calendar(request):
  return 0


def events(request):
  return 0


def logout(request):
  final = redirect('general')
  final.set_cookie('login_status', True, -1)
  return final
