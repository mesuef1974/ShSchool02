
import uuid
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دور"
        verbose_name_plural = "أدوار"

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "صلاحية"
        verbose_name_plural = "صلاحيات"

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ↔ {self.role.name}"

    class Meta:
        unique_together = (("user","role"),)
        verbose_name = "ربط مستخدم بدور"
        verbose_name_plural = "ربط المستخدمين بالأدوار"

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role.name} ↔ {self.permission.code}"

    class Meta:
        unique_together = (("role","permission"),)
        verbose_name = "ربط دور بصلاحية"
        verbose_name_plural = "ربط الأدوار بالصلاحيات"
