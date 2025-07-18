
from django.shortcuts import render

def pharmacy_home(request):
    return render(request, 'pharmacy/home.html')  # adjust the path if needed

