

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.doc_dashboard, name='docdashboard'), 
    path('appointlist/',views.appointment,name='appointment'), 
      path('system/', views.system_settings_view, name='system_settings'),
    path('ward/', views.ward_management_view, name='ward_management'),
     path('ward/icu/', views.icu_page, name='icu'),
    path('ward/general/', views.general_ward, name='general'),
    path('ward/emergency/', views.emergency_ward, name='emergency'),
    path('ward/maternity/', views.maternity_ward, name='maternity'),
    path('ward/covid/', views.covid_isolation, name='covid'),
    path('ward/surgical/',views.surgical_ward,name='surgical'),

]






