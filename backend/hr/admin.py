from django.contrib import admin
from .models import Staff, StaffAttendance, LeaveRequest, DisciplinaryAction, PerformanceReview

admin.site.register(Staff)
admin.site.register(StaffAttendance)
admin.site.register(LeaveRequest)
admin.site.register(DisciplinaryAction)
admin.site.register(PerformanceReview)
