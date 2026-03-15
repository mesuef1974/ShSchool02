from django.contrib import admin
from ..models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'leave_type', 'start_date', 'end_date', 'status')
    search_fields = ('staff__id', 'leave_type', 'status')
    # ...existing code...

