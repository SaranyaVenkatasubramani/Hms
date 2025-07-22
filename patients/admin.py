from django.contrib import admin
from .models import Patient, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'user',
        'dob',
        'emergency_contact_name',
        'emergency_contact_number',
        'qr_code'
    )
    search_fields = ('full_name', 'user__username', 'qr_code')
    list_filter = ('dob',)
    readonly_fields = ('qr_code',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 
        'doctor_name', 
        'consultation_type', 
        'date', 
        'scheduled_time', 
        'status',
        'video_link'
    )
    list_filter = ('consultation_type', 'date', 'status')
    search_fields = ('patient__username', 'doctor__username')
    ordering = ('-date', 'scheduled_time')

    def doctor_name(self, obj):
        return obj.doctor.get_full_name() if obj.doctor else "-"
    doctor_name.short_description = 'Doctor Name'


