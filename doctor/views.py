from django.shortcuts import render
from .models import Doctor
from patients.models import Appointment,Patient
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()



def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


@login_required
def doctor_dashboard(request):
    doctor_user = request.user  # Logged-in doctor
    doctor_name = doctor_user.get_full_name() or doctor_user.username  # Fallback if names not set

    appointments = Appointment.objects.filter(
    doctor=request.user
).select_related('patient', 'patient__userprofile').order_by('date', 'scheduled_time')




    context = {
        'doctor_name': doctor_name,
        'appointments': appointments
    }

    return render(request, 'docdashboard.html', context)

@login_required
def view_patient_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    patient = get_object_or_404(Patient, user=user)
    
    # Fetch appointments linked to this patient user
    appointments = Appointment.objects.filter(patient=user).order_by('date', 'scheduled_time')
    
    context = {
        'patient': patient,
        'appointments': appointments
    }
    return render(request, 'view_patient.html', context)