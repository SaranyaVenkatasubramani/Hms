
from django.shortcuts import render

def admission_dashboard(request):
    return render(request, 'admissions/dashboard.html')
