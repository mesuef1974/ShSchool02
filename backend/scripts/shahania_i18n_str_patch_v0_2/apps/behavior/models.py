import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.people.models import Student

class BehaviorIncident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الواقعة"))
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name=_("الطالب"))
    date = models.DateField(verbose_name=_("تاريخ الواقعة"))
    period = models.SmallIntegerField(null=True, blank=True, verbose_name=_("الحصة"))
    place = models.CharField(max_length=120, blank=True, default="", verbose_name=_("المكان"))
    category = models.CharField(max_length=80, verbose_name=_("نوع الواقعة"))
    description = models.TextField(verbose_name=_("الوصف"))

    def __str__(self):
        return f"{self.student} – {self.date} – {self.category}"

    class Meta:
        verbose_name = _("واقعة سلوكية")
        verbose_name_plural = _("وقائع سلوكية")
