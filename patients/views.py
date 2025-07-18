
from django.shortcuts import render

def patient_login(request):
    return render(request, 'patients/patdashboard.html')

