
from django.shortcuts import render

def doc_dashboard(request):
    return render(request, 'docdashboard.html')
def appointment(request):
    return render(request,'appointlist.html')

def system_settings_view(request):
    return render(request, 'system_settings.html')

def ward_management_view(request):
    return render(request, 'ward_management.html')

def settings_view(request):
    return render(request, 'settings.html')
