from django.urls import path, include
from api import views

urlpatterns = [
  path('getchal/', views.getchal, name='getchal')
]
