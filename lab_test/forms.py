from django import forms
from .models import LabTest
from patients.models import Patient

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient', 'test_name', 'cost', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'style': 'margin-bottom: 15px; padding: 10px; width: 100%;'
            })
