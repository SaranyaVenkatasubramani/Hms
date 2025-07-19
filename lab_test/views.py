
from django.shortcuts import render

def lab_tests(request):
    return render(request, 'lab_test/lab.html')
