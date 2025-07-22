
from django.contrib import admin
from .models import PharmacyItem, DispensedMedicine

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
