from django.contrib import admin
from apps.people.models.enrollment import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "grade",
        "status",
        "class_room_id",
        "school_id",
        "year_id",
        "created_at",
    )

    search_fields = (
        "student_id",
        "grade",
        "status",
        "class_room_id",
        "school_id",
        "year_id",
    )

    list_filter = ("status", "grade")

    ordering = ("student_id",)

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")