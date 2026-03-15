from django.contrib import admin
from apps.behavior.models.behavior_behaviorincident import BehaviorIncident


@admin.register(BehaviorIncident)
class BehaviorIncidentAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "period",
        "place",
        "category",
        "student_id",
        "created_at",
    )

    search_fields = (
        "place",
        "category",
        "student_id",
        "description",
    )

    list_filter = ("category", "period")

    ordering = ("date", "period")

    readonly_fields = ("created_at", "updated_at", "deleted_at", "row_version", "retention_until")