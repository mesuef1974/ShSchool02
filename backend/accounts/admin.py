from django.contrib import admin
from .models import User, Group, UserGroup, Permission, GroupPermission

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Permission)
admin.site.register(GroupPermission)
