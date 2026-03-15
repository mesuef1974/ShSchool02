from django.contrib import admin
from .models import AuditLog, OutboxEvent

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'record_id', 'actor_user', 'action', 'ts')

@admin.register(OutboxEvent)
class OutboxEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'status', 'ts')

