from django.contrib import admin
from apps.audit.models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("table_name", "record_id", "actor_user", "action", "ts")
    search_fields = ("table_name", "record_id", "actor_user", "action")
    ordering = ("ts",)

