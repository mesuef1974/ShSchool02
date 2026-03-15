from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الدور"))
    name = models.CharField(max_length=100, unique=True, verbose_name=_("اسم الدور"))
    description = models.TextField(default="", blank=True, verbose_name=_("الوصف"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ الحذف"))
    row_version = models.IntegerField(default=1, verbose_name=_("إصدار الصف"))

    class Meta:
        verbose_name = _("دور")
        verbose_name_plural = _("الأدوار")
