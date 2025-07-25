
from django.urls import path

from . import views  

urlpatterns = [
    
    path('patient_dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('book/',views.book_appointment,name='book'),
    path('', views.patient_login, name='patient_login'),
    path('patient_form/', views.patient_info_view, name='patient_form'),  
    path('appointment_dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('reschedule/<int:appointment_id>/', views.reschedule_appointment, name='reschedule_appointment'),
    path('prescriptions/', views.view_prescriptions, name='view_prescriptions'),
    path('payment/', views.payment, name='payment'),
    path('payment/proceed/', views.proceed_payment, name='proceed_payment'),

]



    


    



