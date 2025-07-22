from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def homepage(request):
    return render(request, 'index.html')

def get_full_name(self):
    return f"{self.first_name} {self.last_name}".strip()



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
        return redirect('doctor_dashboard')
    elif user.role == 'labtech':
        return redirect('/lab/dashboard/')
    elif user.role == 'pharmacist':
        return redirect('/pharmacy/pharmacy/')
    elif user.role == 'patient':
        return render(request, 'patient_dashboard.html')
    else:
        return redirect('login')



@login_required
def user_settings(request):
    user = request.user
    return render(request, 'settings.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('homepage')  


