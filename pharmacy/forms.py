from django import forms
from .models import PharmacyItem, DispensedMedicine

class InventoryForm(forms.ModelForm):
    class Meta:
        model = PharmacyItem
        fields = ['name', 'quantity', 'expiry_date']

class DispenseMedicineForm(forms.ModelForm):
    class Meta:
        model = DispensedMedicine
        fields = ['prescription_id', 'pharmacy_item', 'quantity_dispensed']


