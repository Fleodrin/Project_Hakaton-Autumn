from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
  path('', views.index, name='general'),
  path('/getdata', views.getdata, name='getdata')
  # path('login/', RedirectView.as_view(url='login', permanent=False)),
]

# urlpatterns += staticfiles_urlpatterns()
