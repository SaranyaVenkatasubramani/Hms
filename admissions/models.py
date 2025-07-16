from django.db import models
from patients.models import Patient
from lab_test.models import LabTest

class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    ward_type = models.CharField(max_length=50)
    admission_date = models.DateTimeField()
    notes = models.TextField()

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_id = models.IntegerField(null=True, blank=True)  # Optional relation
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    billing_date = models.DateTimeField()

class Notification(models.Model):
    recipient_id = models.IntegerField()
    message = models.TextField()
    type = models.CharField(max_length=50)
    sent_at = models.DateTimeField()

