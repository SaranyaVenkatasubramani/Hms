from django.urls import path
from . import views

urlpatterns = [
    path('pharmacy/', views.pharmacy_view, name='pharmacy'),
    
]   
