
from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "date", "period", "status")
    list_filter  = ("date", "status", "period")
    search_fields = ("note",)
    date_hierarchy = "date"
