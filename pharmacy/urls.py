from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy_home, name='pharmacy-home'),
    path('add/', views.add_inventory_item, name='add-inventory'),
    path('dispense/', views.dispense_medicine, name='dispense-medicine'),
]
