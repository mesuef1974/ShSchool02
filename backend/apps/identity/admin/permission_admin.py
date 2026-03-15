from django.contrib import admin
from ..models import Permission

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('code',)

