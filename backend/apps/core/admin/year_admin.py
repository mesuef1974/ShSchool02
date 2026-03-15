from django.contrib import admin
from apps.core.models import Year


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ("label", "school", "start_date", "end_date")
    list_filter = ("school", "label")
    search_fields = ("label", "school__name_ar", "school__moehe_code")
    ordering = ("label",)

    fieldsets = (
        ("بيانات العام الدراسي", {
            "fields": ("school", "label", "start_date", "end_date")
        }),
    )