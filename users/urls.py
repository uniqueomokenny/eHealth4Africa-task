from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
  path('sign-up/', views.SignUp.as_view(), name='signup'),
  path('sign-in/', views.SignInView.as_view(), name='signin'),
  # path('sign-in/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
]
