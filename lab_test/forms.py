from django import forms
from .models import LabTest

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient', 'test_name', 'cost', 'date']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'test_name': forms.Select(attrs={'class': 'form-select'}),
            'cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'dd - mm - yyyy',
                'type': 'date'
            }),
        }