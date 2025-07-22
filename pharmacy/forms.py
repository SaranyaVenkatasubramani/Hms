from django import forms
from .models import PharmacyItem

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



