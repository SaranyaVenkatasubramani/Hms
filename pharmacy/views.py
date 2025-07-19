
from django.shortcuts import render

def pharmacy_home(request):
    return render(request, 'pharmacy.html')  # adjust the path if needed

