

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.doc_dashboard, name='docdashboard'), 
    path('appointlist/',views.appointment,name='appointment'), # Loads at /admissions/
]





