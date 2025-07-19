from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='login'),
    path('signup/',views.signup,name='signup'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('dashboard/', views.redirect_user_dashboard, name='redirect_dashboard')

    path('fpass/',views.forgot_password,name='forgot_password'),
    path('settings/',views.settings,name='settings')
    

]


