
from django.urls import path
from .views import homepage
from .views import login
urlpatterns = [
    path('',views.homepage, name='user-home'),
   
]



