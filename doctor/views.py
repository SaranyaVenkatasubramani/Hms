from django.shortcuts import render
from .models import Doctor

def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


