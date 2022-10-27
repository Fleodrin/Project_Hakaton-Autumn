from django.urls import path

from user import views

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  path('register/', views.RegistrationView.as_view(), name='register'),
  path('logout/', views.logout, name='logout')
]
