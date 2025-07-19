
from django.urls import path
<<<<<<< HEAD
from . import views  

urlpatterns = [
    
    path('patient_dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('doctor/',views.doctor,name='doctor'),
    path('book/',views.book,name='book')
=======
from .import views


urlpatterns = [
    path('', views.patient_login, name='patient_login'),                # /patients/
    
>>>>>>> b34814c21f8604ff29f50f02572edd0904419129
]

