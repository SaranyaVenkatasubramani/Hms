from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request,'fpass.html')

