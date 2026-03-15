from django.db import models
from django.utils.translation import gettext_lazy as _

class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name=_("معرّف السجل"))
    table_name = models.CharField(max_length=120, verbose_name=_("اسم الجدول"))
    record_id = models.CharField(max_length=64, verbose_name=_("معرّف السجل في الجدول"))
    actor_user = models.CharField(max_length=120, verbose_name=_("المستخدم المنفذ"))
    action = models.CharField(max_length=10, verbose_name=_("الإجراء"))
    old_values = models.JSONField(null=True, blank=True, verbose_name=_("القيم القديمة"))
    new_values = models.JSONField(null=True, blank=True, verbose_name=_("القيم الجديدة"))
    ip = models.CharField(max_length=50, blank=True, default="", verbose_name=_("عنوان IP"))
    ua = models.CharField(max_length=200, blank=True, default="", verbose_name=_("وكيل المستخدم"))
    ts = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ ووقت التنفيذ"))

    class Meta:
        verbose_name = _("سجل تدقيق")
        verbose_name_plural = _("سجلات التدقيق")

class OutboxEvent(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name=_("معرّف الحدث"))
    event_type = models.CharField(max_length=120, verbose_name=_("نوع الحدث"))
    payload = models.JSONField(verbose_name=_("البيانات"))
    status = models.CharField(max_length=20, default='pending', verbose_name=_("الحالة"))
    ts = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ ووقت الإنشاء"))

    class Meta:
        verbose_name = _("حدث خارجي")
        verbose_name_plural = _("الأحداث الخارجية")
