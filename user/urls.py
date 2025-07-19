from django.urls import path
from . import views  

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('fpass/',views.forgot_password,name='forgot_password'),
    path('settings/',views.settings,name='settings'),
<<<<<<< HEAD
    
=======
>>>>>>> b34814c21f8604ff29f50f02572edd0904419129
    
]



