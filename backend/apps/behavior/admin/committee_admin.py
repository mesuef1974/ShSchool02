from django.contrib import admin
from apps.behavior.models.behavior_committee import BehaviorCommittee


@admin.register(BehaviorCommittee)
class BehaviorCommitteeAdmin(admin.ModelAdmin):
    list_display = (
        "incident_id",
        "meeting_date",
        "created_at",
    )

    search_fields = (
        "incident_id",
        "notes",
    )

    ordering = ("meeting_date",)

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")