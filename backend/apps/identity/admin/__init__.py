from django.contrib import admin
admin.site.site_header = "لوحة إدارة المدرسة"
admin.site.site_title = "إدارة النظام"
admin.site.index_title = "مرحباً بك في لوحة الإدارة"

from .role_admin import RoleAdmin
from .permission_admin import PermissionAdmin
from .rolepermission_admin import RolePermissionAdmin
from .userrole_admin import UserRoleAdmin
from .rolescope_admin import RoleScopeAdmin
