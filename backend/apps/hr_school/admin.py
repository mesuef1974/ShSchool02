from django.contrib import admin
from .models import LeaveRequest, PerformanceReview

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    pass

