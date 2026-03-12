from django.db import models
from backend.common.models import BaseFormFields

class User(BaseFormFields):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

class Group(BaseFormFields):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)

class UserGroup(BaseFormFields):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Permission(BaseFormFields):
    code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256)

class GroupPermission(BaseFormFields):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
