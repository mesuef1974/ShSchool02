from django.contrib import admin
from apps.behavior.models.behavior_sanction import BehaviorSanction


@admin.register(BehaviorSanction)
class BehaviorSanctionAdmin(admin.ModelAdmin):
    list_display = (
        "incident_id",
        "sanction_type",
        "level",
        "decided_on",
        "executed",
        "created_at",
    )

    search_fields = (
        "incident_id",
        "sanction_type",
    )

    list_filter = ("sanction_type", "executed")

    ordering = ("decided_on",)

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version")