from django.shortcuts import render,redirect
from .models import Appointment
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Patient
from django.shortcuts import get_object_or_404
from .forms import RescheduleForm
from django.contrib import messages



import uuid

def patient_dashboard(request):
    return render(request,'patient_dashboard.html')
def doctor(request):
    return render(request,'doctor.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        consultation_type = request.POST.get('consultation_type')
        date = request.POST.get('date')
        time_str = request.POST.get('scheduled_time')  

        if not doctor_name or not consultation_type or not date or not time_str:
            return render(request, 'book.html', {
                'error': 'Please fill in all required fields.'
            })

        try:
            # Parse the time string to a proper time object
            scheduled_time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            return render(request, 'book.html', {
                'error': 'Invalid time format. Please choose a time from the dropdown.'
            })

        # Save to DB
        Appointment.objects.create(
            patient=request.user,
            doctor_name=doctor_name,
            consultation_type=consultation_type,
            date=date,
            scheduled_time=scheduled_time,
            status='Scheduled',  # You may want to set a default status
            video_link="https://example.com/video123" if consultation_type == "Video" else ""
        )

        return redirect('patient_details_form')

    return render(request, 'book.html')


def patient_login(request):
    return render(request, 'patients/patdashboard.html')


@login_required
def patient_info_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        medical_history = request.POST.get('medical_history')
        allergies = request.POST.get('allergies')
        emergency_name = request.POST.get('emergency_contact')
        emergency_number = request.POST.get('emergency_number')

        # Generate unique patient ID
        patient_id = str(uuid.uuid4())

        # Save to DB
        Patient.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            dob=dob,
            medical_history=medical_history,
            allergies=allergies,
            emergency_contact_name=emergency_name,
            emergency_contact_number=emergency_number,
            qr_code=patient_id,
        )

        return redirect('patient_dashboard')  # change to your actual dashboard

    return render(request, 'patient_form.html')


@login_required
def appointment_dashboard(request):
    appointments = Appointment.objects.filter(patient=request.user).order_by('-date')
    return render(request, 'appointment_dashboard.html', {'appointments': appointments})


def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Only allow cancellation via GET or POST as you wish
    appointment.delete()
    messages.success(request, 'Appointment cancelled successfully.')
    return redirect('appointment_dashboard')


def reschedule_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        new_date = request.POST.get('date')
        new_time = request.POST.get('time')
        appointment.date = new_date
        appointment.scheduled_time = new_time
        appointment.save()
        return redirect('appointment_dashboard')

    return render(request, 'reschedule.html', {'appointment': appointment})

