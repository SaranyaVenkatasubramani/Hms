from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('receptionist', 'Receptionist'),
        ('doctor', 'Doctor'),
        ('labtech', 'Lab Technician'),
        ('pharmacist', 'Pharmacist'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()
    qr_code = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=255)
