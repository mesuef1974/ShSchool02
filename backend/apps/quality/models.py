from django.db import models
from django.utils.translation import gettext_lazy as _

class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الدليل"))
    domain = models.CharField(max_length=80, verbose_name=_("المجال"))
    title = models.CharField(max_length=200, verbose_name=_("العنوان"))
    description = models.TextField(blank=True, default="", verbose_name=_("الوصف"))
    file_link = models.CharField(max_length=500, blank=True, default="", verbose_name=_("رابط الملف"))

    class Meta:
        verbose_name = _("دليل جودة")
        verbose_name_plural = _("أدلة الجودة")

class ImprovementPlan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الخطة"))
    objective = models.CharField(max_length=300, verbose_name=_("الهدف"))
    owner = models.CharField(max_length=120, verbose_name=_("المسؤول"))
    start_date = models.DateField(verbose_name=_("تاريخ البدء"))
    end_date = models.DateField(verbose_name=_("تاريخ الانتهاء"))
    progress = models.SmallIntegerField(default=0, verbose_name=_("التقدم"))

    class Meta:
        verbose_name = _("خطة تحسين")
        verbose_name_plural = _("خطط التحسين")

class KpiSnapshot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف المؤشر"))
    name = models.CharField(max_length=120, verbose_name=_("اسم المؤشر"))
    value = models.DecimalField(max_digits=12, decimal_places=4, verbose_name=_("القيمة"))
    taken_on = models.DateField(verbose_name=_("تاريخ القياس"))

    class Meta:
        verbose_name = _("لقطة مؤشر أداء")
        verbose_name_plural = _("لقطات مؤشرات الأداء")
