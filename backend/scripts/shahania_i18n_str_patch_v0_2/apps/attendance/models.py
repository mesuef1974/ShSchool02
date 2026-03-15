import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.people.models import Enrollment, Staff

class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف السجل"))
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name=_("قيد الطالب"))
    date = models.DateField(verbose_name=_("تاريخ الحضور"))
    period = models.SmallIntegerField(verbose_name=_("الحصة"))
    status = models.CharField(max_length=10, choices=(("present","حاضر"),("absent","غائب"),("late","متأخر"),("excused","معذور")), verbose_name=_("حالة الحضور"))
    note = models.TextField(blank=True, default="", verbose_name=_("ملاحظات"))

    def __str__(self):
        return f"{self.enrollment.student} – {self.date} – حصة {self.period} – {self.status}"

    class Meta:
        unique_together = (("enrollment","date","period"),)
        verbose_name = _("سجل حضور طالب")
        verbose_name_plural = _("سجلات حضور الطلبة")
