from django.contrib import admin
from .models import Role, Permission, RolePermission, UserRole, RoleScope

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    pass

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(RoleScope)
class RoleScopeAdmin(admin.ModelAdmin):
    pass

