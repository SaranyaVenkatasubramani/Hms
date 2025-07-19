from django.urls import path
from .import views 

urlpatterns = [
    path('',views.lab_tests, name='lab-tests'),
]
