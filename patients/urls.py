
from django.urls import path
from .import views


urlpatterns = [
    path('', views.patient_login, name='patient_login'),                # /patients/
    
]

