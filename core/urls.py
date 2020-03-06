from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('add-medical-info/', views.MedicalInfoView.as_view(), name='add-medical-info'),
  path('statistical-details/', views.statistical_details, name='statistical-details'),
  path('medical-recodes/', views.medical_recodes, name='medical-recodes'),
]
