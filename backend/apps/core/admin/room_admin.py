from django.contrib import admin
from apps.core.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("code", "school", "room_type", "capacity")
    list_filter = ("school", "room_type")
    search_fields = ("code", "school__name_ar", "room_type")
    ordering = ("code",)

    fieldsets = (
        ("بيانات الغرفة", {
            "fields": (
                "school",
                "code",
                "room_type",
                "capacity",
            )
        }),
    )