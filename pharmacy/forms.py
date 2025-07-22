from django import forms
from .models import PharmacyItem
from pharmacy.models import Prescription

class PharmacyItemForm(forms.ModelForm):
    class Meta:
        model = PharmacyItem
        fields = ['name', 'quantity']
        widgets = {   
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter drug name',
                'class': 'form-control'
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Enter quantity',
                'class': 'form-control'
            }),
        }     


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['symptoms', 'diagnosis', 'medications', 'notes']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 2}),
            'diagnosis': forms.Textarea(attrs={'rows': 2}),
            'medications': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
