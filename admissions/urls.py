
from django.urls import path
from .views import admission_dashboard

urlpatterns = [
    path('admissions', admission_dashboard, name='admissions-dashboard'),
]
