from django.contrib import admin
from apps.core.models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("code", "label_ar", "label_en")
    search_fields = ("code", "label_ar", "label_en")
    ordering = ("code",)

    fieldsets = (
        ("بيانات الصف", {
            "fields": ("code", "label_ar", "label_en")
        }),
    )