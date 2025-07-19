from django.contrib import admin
from .models import PharmacyItem, DispensedMedicine

admin.site.register(PharmacyItem)
admin.site.register(DispensedMedicine)
