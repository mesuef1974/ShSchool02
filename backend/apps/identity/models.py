from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, default="")

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user','role'),)

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('role','permission'),)
