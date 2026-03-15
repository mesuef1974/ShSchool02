from django.contrib import admin
from apps.attendance.models.attendance_record import AttendanceRecord


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = (
        "enrollment_id",
        "date",
        "period",
        "status",
        "created_at",
    )

    search_fields = (
        "enrollment_id",
        "status",
        "date",
    )

    list_filter = ("status", "period")

    ordering = ("date", "period")

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")