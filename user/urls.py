
from django.urls import path
from .views import homepage
from .views import login
urlpatterns = [
    path('', homepage, name='user-home'),
    path('login', login,name='user-login'),
]



