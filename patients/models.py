from django.db import models
from user.models import CustomUser

class Patient(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    status = models.CharField(max_length=50)
    medical_history = models.TextField()
    qr_code = models.CharField(max_length=255)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_time = models.TimeField()
    status = models.CharField(max_length=50)
    video_link = models.URLField()

