
from django.urls import path
from .import views
urlpatterns = [
    path('',views.pharmacy_home, name='pharmacy-home'),
]
