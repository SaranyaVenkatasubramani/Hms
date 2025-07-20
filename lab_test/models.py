
from django.db import models
import datetime
from patients.models import Patient  # Assuming you're using a separate patients app

class LabTest(models.Model):
    TEST_CHOICES = [
        ('Blood Test', 'Blood Test'),
        ('X-Ray', 'X-Ray'),
        ('MRI', 'MRI'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    test_name = models.CharField(max_length=50, choices=TEST_CHOICES,null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.test_name} - {self.patient.name}"

