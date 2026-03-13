from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_teacher', 'is_student')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_teacher', 'is_student')
    
    # Add custom fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('is_teacher', 'is_student', 'is_parent', 'national_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Roles', {'fields': ('is_teacher', 'is_student', 'is_parent', 'national_id')}),
    )
