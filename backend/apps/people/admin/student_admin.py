from django.contrib import admin
from apps.people.models.student import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name_ar",
        "last_name_ar",
        "first_name_en",
        "last_name_en",
        "gender",
        "phone",
        "email",
        "nationality_code",
        "created_at",
    )

    search_fields = (
        "first_name_ar",
        "last_name_ar",
        "first_name_en",
        "last_name_en",
        "national_id",
        "phone",
        "email",
    )

    list_filter = ("gender", "nationality_code")

    ordering = ("first_name_ar", "last_name_ar")

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")