from django.contrib import admin
from .models import Staff, StaffAttendance, LeaveRequest, PerformanceReview

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'hire_date')
    search_fields = ('user__username', 'job_title')
    list_filter = ('job_title',)

@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('date', 'status')
    autocomplete_fields = ['staff']
    date_hierarchy = 'date'

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('staff', 'leave_type', 'date_from', 'date_to', 'status')
    list_filter = ('leave_type', 'status')
    autocomplete_fields = ['staff']

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('staff', 'overall', 'created_at')
    list_filter = ('overall',)
    autocomplete_fields = ['staff']
