from django import forms
from .models import Appointment

class RescheduleForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'scheduled_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'scheduled_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
