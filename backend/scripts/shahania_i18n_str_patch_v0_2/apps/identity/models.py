import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الدور"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("اسم الدور"))
    description = models.TextField(blank=True, default="", verbose_name=_("الوصف"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("دور")
        verbose_name_plural = _("أدوار")

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الصلاحية"))
    code = models.CharField(max_length=150, unique=True, verbose_name=_("رمز الصلاحية"))
    description = models.TextField(blank=True, default="", verbose_name=_("الوصف"))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("صلاحية")
        verbose_name_plural = _("صلاحيات")

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("المستخدم"))
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name=_("الدور"))

    def __str__(self):
        return f"{self.user.username} ↔ {self.role.name}"

    class Meta:
        unique_together = (("user","role"),)
        verbose_name = _("ربط مستخدم بدور")
        verbose_name_plural = _("ربط المستخدمين بالأدوار")

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name=_("الدور"))
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name=_("الصلاحية"))

    def __str__(self):
        return f"{self.role.name} ↔ {self.permission.code}"

    class Meta:
        unique_together = (("role","permission"),)
        verbose_name = _("ربط دور بصلاحية")
        verbose_name_plural = _("ربط الأدوار بالصلاحيات")
