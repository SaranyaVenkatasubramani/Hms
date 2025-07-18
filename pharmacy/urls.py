
from django.urls import path
from .views import pharmacy_home

urlpatterns = [
    path('pharmacy', pharmacy_home, name='pharmacy-home'),
]
