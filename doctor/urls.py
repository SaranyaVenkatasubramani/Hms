from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view-patient/<int:pk>/', views.view_patient_details, name='view_patient_details'),
    path('write-prescription/<int:appointment_id>/', views.write_prescription, name='write_prescription'),

]
