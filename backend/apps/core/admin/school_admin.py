from django.contrib import admin
from apps.core.models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name_ar", "moehe_code")
    search_fields = ("name_ar", "name_en", "moehe_code")
    ordering = ("name_ar",)

    fieldsets = (
        ("بيانات المدرسة", {
            "fields": ("name_ar", "name_en", "moehe_code")
        }),
    )