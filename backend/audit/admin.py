from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('ts', 'actor', 'action', 'entity', 'entity_id')
    list_filter = ('action', 'entity', 'ts')
    search_fields = ('actor__username', 'entity')
    date_hierarchy = 'ts'
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
