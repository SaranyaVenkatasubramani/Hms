
from django.shortcuts import render

def doc_dashboard(request):
    return render(request, 'docdashboard.html')
def appointment(request):
    return render(request,'appointlist.html')

def system_settings_view(request):
    return render(request, 'system_settings.html')

def ward_management_view(request):
    return render(request, 'ward_management.html')


def icu_page(request):
    return render(request, 'ICU.html')
def general_ward(request):
    return render(request, 'general.html')

def emergency_ward(request):
    return render(request, 'emergency.html')

def maternity_ward(request):
    return render(request, 'maternity.html')

def covid_isolation(request):
    return render(request, 'covid.html')
def surgical_ward(request):
    return render(request,'surgical.html')
