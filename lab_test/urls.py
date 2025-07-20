from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_lab_test, name='add_lab_test'),
]
