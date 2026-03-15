from django.contrib import admin
from apps.core.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name_ar", "name_en")
    search_fields = ("name_ar", "name_en")
    ordering = ("name_ar",)

    fieldsets = (
        ("بيانات المادة", {
            "fields": ("name_ar", "name_en")
        }),
    )