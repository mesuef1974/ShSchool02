from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import UserRole, RolePermission

class HasRBACPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            verb='read'
        elif request.method=='POST':
            verb='create'
        elif request.method in ('PUT','PATCH'):
            verb='update'
        elif request.method=='DELETE':
            verb='delete'
        else:
            verb='read'
        resource=getattr(view,'permission_resource',None)
        if not resource:
            return True
        required=f"{resource}.{verb}"
        roles=UserRole.objects.filter(user=request.user).values_list('role_id', flat=True)
        perms=set(RolePermission.objects.filter(role_id__in=roles).values_list('permission__code', flat=True))
        return required in perms
