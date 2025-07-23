"""
URL configuration for hospital_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admissions import views as admissions_views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include('user.urls')),          
    path('pharmacy/', include('pharmacy.urls')),
    path('admissions/', include('admissions.urls')),
    path('patients/', include('patients.urls')),
    path('lab/', include('lab_test.urls')),
    path('doctor/', include('doctor.urls')),
    path('general/', admissions_views.general_ward, name='general_direct'),
    path('emergency/', admissions_views.emergency_ward, name='emergency_direct'),
    path('maternity/', admissions_views.maternity_ward, name='maternity_direct'),
    path('covid/', admissions_views.covid_isolation, name='covid_direct'),
    path('icu/', admissions_views.icu_page, name='icu_direct'),
    path('surgery/', admissions_views.surgical_ward, name='surgical_direct'),
]


