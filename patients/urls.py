
from django.urls import path

from . import views  

urlpatterns = [
    
    path('patient_dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('book/',views.book_appointment,name='book'),
    path('', views.patient_login, name='patient_login'),
    path('patient-form/', views.patient_info_view, name='patient_details_form'),  
    path('appointment_dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('reschedule/<int:appointment_id>/', views.reschedule_appointment, name='reschedule_appointment'),
]    

    


    



