from django.db import models
from django.utils.translation import gettext_lazy as _

class TransportStudentRider(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الراكب"))
    route_id = models.UUIDField(verbose_name=_("معرّف المسار"))
    student_id = models.UUIDField(verbose_name=_("معرّف الطالب"))
    pickup_stop_id = models.UUIDField(null=True, blank=True, verbose_name=_("محطة الصعود"))
    dropoff_stop_id = models.UUIDField(null=True, blank=True, verbose_name=_("محطة النزول"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاريخ التحديث"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("تاريخ الحذف"))
    row_version = models.IntegerField(default=1, verbose_name=_("إصدار الصف"))

    class Meta:
        db_table = "transport_studentrider"
        managed = True
        unique_together = ("student_id", "route_id")
        verbose_name = _("راكب نقل")
        verbose_name_plural = _("ركاب النقل")
