from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile
from django.contrib.auth.models import Group

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
   class CustomUserAdmin(BaseUserAdmin):  
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']
 
admin.site.unregister(Group)  


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'emergency_contact', 'qr_code')
    search_fields = ('user__username', 'phone', 'emergency_contact')

