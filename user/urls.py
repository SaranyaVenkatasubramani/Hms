from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='login'),
    path('signup/',views.signup,name='signup'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    path('dashboard/', views.redirect_user_dashboard, name='redirect_dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('settings/', views.user_settings, name='settings'),



]


