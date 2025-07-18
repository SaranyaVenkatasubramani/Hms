
from django.urls import path
from .views import lab_tests

urlpatterns = [
    path('lab', lab_tests, name='lab-tests'),
]
