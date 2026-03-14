import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.identity.models import Role, Permission, RolePermission

class Command(BaseCommand):
    help='Load roles & permissions from rbac/roles_permissions.json into DB'
    def handle(self, *args, **kwargs):
        path=Path(settings.BASE_DIR)/'rbac'/'roles_permissions.json'
        data=json.loads(path.read_text(encoding='utf-8'))
        roles={}
        for r in data.get('roles',[]):
            role,_=Role.objects.get_or_create(name=r)
            roles[r]=role
        for res,verbs in data.get('permissions',{}).items():
            for v in verbs:
                code=f"{res}.{v}"
                perm,_=Permission.objects.get_or_create(code=code)
                for role in roles.values():
                    RolePermission.objects.get_or_create(role=role, permission=perm)
        self.stdout.write(self.style.SUCCESS('RBAC loaded.'))
