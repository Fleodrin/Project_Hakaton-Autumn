from django.urls import path, include

from news import views

urlpatterns = [
  path('', views.news, name='news'),
  path('<int:_id>/', views.news_detail, name='news_detail'),
  path('create/', views.NewsCreateView.as_view(), name='news_create.html'),
]
