from django.shortcuts import render,redirect
from .models import Appointment
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Patient
from django.shortcuts import get_object_or_404
from .forms import RescheduleForm
from django.contrib import messages
import uuid
from user.models import CustomUser
from pharmacy.models import Prescription

@login_required
def book_appointment(request):
    if request.method == 'POST':
        # collect form data
        doctor_name = request.POST.get('doctor_name')
        consultation_type = request.POST.get('consultation_type')
        date = request.POST.get('date')
        time_str = request.POST.get('scheduled_time')

        return redirect(f"/patients/patient_form/?doctor_name={doctor_name}&consultation_type={consultation_type}&date={date}&scheduled_time={time_str}")


    
    # for GET, show form
    return render(request, 'book.html', {
        'doctor_name': request.GET.get('doctor_name', ''),
        'specialization': request.GET.get('specialization', ''),
        'hospital': request.GET.get('hospital', ''),
        'rating': request.GET.get('rating', ''),
        'fee': request.GET.get('fee', ''),
        'address': request.GET.get('address', '')
    })



def patient_dashboard(request):
    return render(request,'patient_dashboard.html')
def doctor(request):
    return render(request,'doctor.html')



def patient_login(request):
    return render(request, 'patients/patdashboard.html')


@login_required
def patient_info_view(request):
    if request.method == 'POST':
        # Patient info from form
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        medical_history = request.POST.get('medical_history')
        allergies = request.POST.get('allergies')
        emergency_name = request.POST.get('emergency_contact')
        emergency_number = request.POST.get('emergency_number')

        # Appointment info from hidden fields
        doctor_name = request.POST.get('doctor_name')
        consultation_type = request.POST.get('consultation_type')
        date = request.POST.get('date')
        scheduled_time = request.POST.get('scheduled_time')

        # Create or update patient
        patient_obj, created = Patient.objects.get_or_create(
            user=request.user,
            defaults={
                'full_name': full_name,
                'address': address,
                'dob': dob,
                'medical_history': medical_history,
                'allergies': allergies,
                'emergency_contact_name': emergency_name,
                'emergency_contact_number': emergency_number,
                'qr_code': str(uuid.uuid4()),
            }
        )

        # Get doctor object
        doctor = CustomUser.objects.filter(first_name=doctor_name, role='doctor').first()


        if not doctor:
            messages.error(request, 'Doctor not found.')
            return redirect('book')  # or handle differently

        # Create Appointment
        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            consultation_type=consultation_type,
            date=date,
            scheduled_time=scheduled_time,
            status='Scheduled',
            video_link="https://example.com/video123" if consultation_type == "Video" else ""
        )

        return redirect('appointment_dashboard')

    # If GET, get appointment data from query params
    return render(request, 'patient_form.html', {
        'doctor_name': request.GET.get('doctor_name', ''),
        'consultation_type': request.GET.get('consultation_type', ''),
        'date': request.GET.get('date', ''),
        'scheduled_time': request.GET.get('scheduled_time', '')
    })

@login_required
def appointment_dashboard(request):
    user = request.user
    if user.role == 'patient':
        appointments = Appointment.objects.filter(patient=user).order_by('-date', '-scheduled_time')
    elif user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor=user).order_by('-date', '-scheduled_time')
    else:
        appointments = Appointment.objects.none()  # or show all if admin/superadmin

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

from pharmacy.models import Prescription

def view_prescriptions(request):
    patient = request.user.patient  # assumes you're using a Patient model linked to CustomUser
    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date_created')

    return render(request, 'patient_prescriptions.html', {
        'prescriptions': prescriptions
    })
@login_required
def payment(request):
    return render(request, 'payment.html')
@login_required
def proceed_payment(request):
    return render(request, 'proceed_payment.html')