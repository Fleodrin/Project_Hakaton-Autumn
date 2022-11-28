

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from django.conf import settings

from django.views.static import serve

from web import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('general/', include('web.urls'), name='general'),
  path('', RedirectView.as_view(url='/general/', permanent=False)),
  path('news/', include('news.urls')),
  path('calendar/', views.calendar, name='calendar'),
  path('events', views.events, name='events'),
  path('user/', include('user.urls')),
  path('api/',include('api.urls'),name='api'),
  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
  path('ckeditor/', include('ckeditor_uploader.urls'))
]
