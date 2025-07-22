from django.db import models
from user.models import CustomUser
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model() 


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    medical_history = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, default='', blank=True)
    emergency_contact_number = models.CharField(max_length=15, default='', blank=True)
    qr_code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"


class Appointment(models.Model):
    CONSULTATION_TYPE = (
        ('Video', 'Video'),
        ('Clinic', 'Clinic')
    )

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPE, default='Clinic')
    date = models.DateField(default=timezone.now)
    scheduled_time = models.TimeField()
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True,limit_choices_to={'role': 'doctor'})
    video_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        doctor_name = self.doctor.get_full_name() if self.doctor else 'No doctor'
        return f"{self.patient.username} - {doctor_name} - {self.consultation_type}"

         
