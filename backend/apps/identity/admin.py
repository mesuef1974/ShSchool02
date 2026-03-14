
from django.contrib import admin
from .models import Role, Permission, UserRole, RolePermission

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("code",)
    search_fields = ("code",)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter  = ("role",)
    search_fields = ("user__username", "role__name")

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("role", "permission")
    list_filter  = ("role",)
    search_fields = ("role__name", "permission__code")
