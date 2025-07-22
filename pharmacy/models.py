


from django.db import models

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