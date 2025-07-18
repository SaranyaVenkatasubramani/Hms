
from django.shortcuts import render

def homepage(request):
    return render(request, 'user/index.html')
def login(request):
    return render(request,'user/login.html')

# Create your views here.
