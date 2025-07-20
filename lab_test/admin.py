
from django.contrib import admin
from .models import LabTest
from patients.models import Patient

@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    autocomplete_fields = ['patient']
