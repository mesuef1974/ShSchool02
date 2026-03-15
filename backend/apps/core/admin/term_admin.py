from django.contrib import admin
from apps.core.models import Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("code", "year", "start_date", "end_date")
    list_filter = ("year", "code")
    search_fields = ("code", "year__label", "year__school__name_ar")
    ordering = ("year__label", "code")

    fieldsets = (
        ("بيانات الفصل الدراسي", {
            "fields": (
                "year",
                "code",
                "start_date",
                "end_date",
            )
        }),
    )