from django.db import models
from django.utils.translation import gettext_lazy as _

class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الدليل"))
    opi_id = models.UUIDField(null=True, blank=True, verbose_name=_("معرّف OPI"))
    kpi_code = models.CharField(max_length=60, null=True, blank=True, verbose_name=_("رمز KPI"))
    evidence_type = models.CharField(max_length=120, null=True, blank=True, verbose_name=_("نوع الدليل"))
    link = models.TextField(null=True, blank=True, verbose_name=_("رابط الدليل"))
    notes = models.TextField(null=True, blank=True, verbose_name=_("ملاحظات"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ الحذف"))
    row_version = models.IntegerField(default=1, verbose_name=_("إصدار الصف"))

    class Meta:
        verbose_name = _("دليل جودة")
        verbose_name_plural = _("أدلة الجودة")
