from django.contrib import admin
from apps.audit.models import OutboxEvent

@admin.register(OutboxEvent)
class OutboxEventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "status", "ts")
    search_fields = ("event_type", "status")
    ordering = ("ts",)

