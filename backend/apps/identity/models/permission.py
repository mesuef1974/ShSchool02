from django.db import models
from django.utils.translation import gettext_lazy as _

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الصلاحية"))
    code = models.CharField(max_length=150, unique=True, verbose_name=_("رمز الصلاحية"))
    description = models.TextField(default="", blank=True, verbose_name=_("الوصف"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ الحذف"))
    row_version = models.IntegerField(default=1, verbose_name=_("إصدار الصف"))

    class Meta:
        verbose_name = _("صلاحية")
        verbose_name_plural = _("الصلاحيات")
