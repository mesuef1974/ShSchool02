
from django.contrib import admin
from apps.people.models.guardian import Guardian


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = (
        "first_name_ar",
        "last_name_ar",
        "phone",
        "email",
        "relation_to_student",
        "created_at",
    )

    search_fields = (
        "first_name_ar",
        "last_name_ar",
        "phone",
        "email",
        "relation_to_student",
    )

    list_filter = ("relation_to_student",)

    ordering = ("first_name_ar", "last_name_ar")

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")
