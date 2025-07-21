from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.add_lab_test, name='add_lab_test'),  # ✅ change '' to 'dashboard/'
]