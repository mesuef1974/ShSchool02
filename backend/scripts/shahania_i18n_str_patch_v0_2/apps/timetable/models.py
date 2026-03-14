
import uuid
from django.db import models
from apps.core.models import ClassRoom, Subject, Room
from apps.people.models import Staff

class TimetableRule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "قاعدة جدول"
        verbose_name_plural = "قواعد الجدول"

class TimetableSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    day_of_week = models.SmallIntegerField()
    period = models.SmallIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.class_room} – يوم {self.day_of_week} – حصّة {self.period} – {self.subject}"

    class Meta:
        unique_together = (("class_room","day_of_week","period"),)
        verbose_name = "حصة"
        verbose_name_plural = "الحصص"
