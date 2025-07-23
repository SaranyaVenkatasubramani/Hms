from patients.models import Appointment,Patient
from django.db import models
from user.models import CustomUser

class PharmacyItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.quantity} units"

class DispensedMedicine(models.Model):
    prescription_id = models.CharField(max_length=50)
    pharmacy_item = models.ForeignKey(PharmacyItem, on_delete=models.CASCADE)
    quantity_dispensed = models.PositiveIntegerField()
    dispensed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prescription_id} - {self.pharmacy_item.name}"

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    symptoms = models.TextField()
    diagnosis = models.TextField()
    medications = models.TextField()
    notes = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.date_created.strftime('%d %b %Y')}"