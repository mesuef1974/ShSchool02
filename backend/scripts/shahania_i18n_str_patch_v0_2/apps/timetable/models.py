import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import ClassRoom, Subject, Room
from apps.people.models import Staff

class TimetableRule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف القاعدة"))
    name = models.CharField(max_length=120, verbose_name=_("اسم القاعدة"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("قاعدة جدول")
        verbose_name_plural = _("قواعد الجدول")

class TimetableSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الحصة"))
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT, verbose_name=_("الغرفة الصفية"))
    day_of_week = models.SmallIntegerField(verbose_name=_("اليوم"))
    period = models.SmallIntegerField(verbose_name=_("الحصة"))
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name=_("المادة"))
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT, verbose_name=_("المعلم"))
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True, verbose_name=_("الغرفة"))

    def __str__(self):
        return f"{self.class_room} – يوم {self.day_of_week} – حصّة {self.period} – {self.subject}"

    class Meta:
        unique_together = (("class_room","day_of_week","period"),)
        verbose_name = _("حصة")
        verbose_name_plural = _("الحصص")
