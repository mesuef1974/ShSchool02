import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.people.models import Student

class ClinicVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الزيارة"))
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name=_("الطالب"))
    date = models.DateField(verbose_name=_("تاريخ الزيارة"))
    reason = models.CharField(max_length=200, verbose_name=_("سبب الزيارة"))
    details_enc = models.BinaryField(null=True, blank=True, verbose_name=_("تفاصيل مشفرة"))

    def __str__(self):
        return f"عيادة: {self.student} – {self.date} – {self.reason}"

    class Meta:
        verbose_name = _("زيارة عيادة")
        verbose_name_plural = _("زيارات العيادة")
