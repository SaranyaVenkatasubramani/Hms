
from django.contrib import admin
from .models import PharmacyItem, DispensedMedicine
from .models import Prescription

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment', 'date_created')
    list_filter = ('doctor', 'date_created')
    search_fields = ('patient__full_name', 'doctor__full_name', 'symptoms', 'diagnosis', 'medications')
    ordering = ('-date_created',)

@admin.register(PharmacyItem)
class PharmacyItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'added_on')
    search_fields = ('name',)
    list_filter = ('added_on',)

@admin.register(DispensedMedicine)
class DispensedMedicineAdmin(admin.ModelAdmin):
    list_display = ('prescription_id', 'pharmacy_item', 'quantity_dispensed', 'dispensed_date')
    search_fields = ('prescription_id', 'pharmacy_item__name')
    list_filter = ('dispensed_date',)
