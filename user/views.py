from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from patients.models import Appointment,Patient
from doctor.models import Doctor
from admissions.models import Admission
from django.shortcuts import render
from django.utils import timezone
from patients.models import Appointment



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
         total_patients = Patient.objects.count()
         total_doctors = Doctor.objects.count()
         total_admissions = Appointment.objects.count()

         admission_rate = round((total_admissions / total_patients * 100), 1) if total_patients > 0 else 0

         appointments = Appointment.objects.select_related('patient', 'doctor').order_by('date', 'scheduled_time')


         # Combine all into context
         context = {
            'total_patients': total_patients,
            'total_doctors': total_doctors,
            'admission_rate': admission_rate,
             'appointments': appointments,

         }



         return render(request, 'admin.html', context)

    elif user.role == 'receptionist':
        appointments = Appointment.objects.select_related('patient', 'doctor').order_by('date', 'scheduled_time')
        return render(request, 'receptionist_dashboard.html', {'appointments': appointments})
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


