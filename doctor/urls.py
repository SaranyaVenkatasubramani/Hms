from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view-patient/<int:pk>/', views.view_patient_details, name='view_patient_details'),
]
