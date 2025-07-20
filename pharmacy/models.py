from django.db import models

class PharmacyItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiry_date = models.DateTimeField()

    def __str__(self):
        return self.name

class DispensedMedicine(models.Model):
    prescription_id = models.CharField(max_length=100)
    pharmacy_item = models.ForeignKey(PharmacyItem, on_delete=models.CASCADE)
    quantity_dispensed = models.IntegerField()
    dispensed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prescription_id} - {self.pharmacy_item.name}"


