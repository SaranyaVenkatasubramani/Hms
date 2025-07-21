from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def homepage(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('redirect_dashboard') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('redirect_dashboard')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def redirect_user_dashboard(request):
    user = request.user

    if user.role == 'superadmin':
        return render(request, 'admin.html')
    elif user.role == 'receptionist':
        return render(request, 'prescription.html')
    elif user.role == 'doctor':
        return render(request, 'docdashboard.html')
    elif user.role == 'labtech':
        return render(request, 'lab.html')
    elif user.role == 'pharmacist':
        return render(request, 'pharmacy.html')
    elif user.role == 'patient':
        return render(request, 'patient_dashboard.html')
    else:
        return redirect('login')

def forgot_password(request):
    return render(request,'fpass.html')

def settings(request):
    return render(request,'settings.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')  


