from django.shortcuts import render,get_object_or_404,redirect
from .models import Doctor
from patients.models import Appointment,Patient
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from pharmacy.forms import PrescriptionForm  # or wherever your form lives
from user.models import CustomUser
from pharmacy.models import Prescription

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



@login_required
def write_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    patient = appointment.patient
    doctor = request.user

    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.appointment = appointment
            prescription.patient = Patient.objects.get(user=appointment.patient)
            prescription.doctor = doctor
            prescription.save()
            messages.success(request, "Prescription saved successfully.")
            return redirect('doctor_dashboard')
    else:
        form = PrescriptionForm()

    return render(request, 'write_prescription.html', {
        'form': form,
        'appointment': appointment,
        'patient': patient
    })