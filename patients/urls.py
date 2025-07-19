
from django.urls import path

from . import views  

urlpatterns = [
    
    path('patient_dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('doctor/',views.doctor,name='doctor'),
    path('book/',views.book,name='book'),
    path('', views.patient_login, name='patient_login'),     
]
    


