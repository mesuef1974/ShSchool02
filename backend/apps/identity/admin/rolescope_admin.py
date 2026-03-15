from django.contrib import admin
from ..models import RoleScope

@admin.register(RoleScope)
class RoleScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'school', 'year', 'class_room', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('user__username', 'role__name')

