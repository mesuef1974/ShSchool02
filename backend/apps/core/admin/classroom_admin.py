from django.contrib import admin
from apps.core.models import ClassRoom


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("school", "year", "grade", "section")
    list_filter = ("school", "year", "grade")
    search_fields = (
        "section",
        "school__name_ar",
        "year__label",
        "grade__label_ar",
    )
    ordering = ("grade__code", "section")

    fieldsets = (
        ("بيانات الشعبة", {
            "fields": (
                "school",
                "year",
                "grade",
                "section",
            )
        }),
    )