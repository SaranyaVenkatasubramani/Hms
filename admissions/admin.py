from django.contrib import admin
from .models import Admission, Billing, Notification

admin.site.register(Admission)
admin.site.register(Billing)
admin.site.register(Notification)

