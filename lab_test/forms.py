

from django import forms
from .models import LabTest

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient', 'test_name', 'cost', 'date']
