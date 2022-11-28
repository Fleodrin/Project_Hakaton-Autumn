from django.urls import path, include
from api import views

urlpatterns = [
  path('getchal/<str:_symb>', views.getchal, name='getchal')
]
