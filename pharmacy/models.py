from django.db import models

class PharmacyItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    expiry_date = models.DateTimeField()

class DispensedMedicine(models.Model):
    prescription_id = models.IntegerField()  # OR make a Prescription model
    pharmacy_item = models.ForeignKey(PharmacyItem, on_delete=models.CASCADE)
    quantity_dispensed = models.FloatField()
    dispensed_date = models.DateTimeField()

