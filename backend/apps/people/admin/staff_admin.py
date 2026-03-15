from django.contrib import admin
from apps.people.models.staff import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "first_name_ar",
        "last_name_ar",
        "job_title",
        "department",
        "email",
        "phone",
        "status",
        "created_at",
    )

    search_fields = (
        "first_name_ar",
        "last_name_ar",
        "job_title",
        "department",
        "email",
        "phone",
        "status",
    )

    list_filter = ("department", "status")

    ordering = ("first_name_ar", "last_name_ar")

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")