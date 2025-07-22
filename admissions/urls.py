

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.doc_dashboard, name='docdashboard'), 
    path('appointlist/',views.appointment,name='appointment'), 
      path('system/', views.system_settings_view, name='system_settings'),
    path('ward/', views.ward_management_view, name='ward_management'),
    path('settings/', views.settings_view, name='settings'),# Loads at /admissions/
]






