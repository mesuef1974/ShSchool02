from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'date', 'period', 'status')
    list_filter = ('date', 'status', 'enrollment__grade')
    search_fields = ('enrollment__student__national_id', 'enrollment__student__first_name_ar')
    autocomplete_fields = ['enrollment']
    date_hierarchy = 'date'
