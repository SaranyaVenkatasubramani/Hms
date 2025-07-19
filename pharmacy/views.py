
from django.shortcuts import render

def pharmacy_home(request):
    return render(request, 'prescription.html')  # adjust the path if needed

