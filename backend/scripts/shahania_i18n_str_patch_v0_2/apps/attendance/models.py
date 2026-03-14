
import uuid
from django.db import models
from apps.people.models import Enrollment, Staff

class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    period = models.SmallIntegerField()
    status = models.CharField(max_length=10, choices=(("present","حاضر"),("absent","غائب"),("late","متأخر"),("excused","معذور")))
    note = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.enrollment.student} – {self.date} – حصة {self.period} – {self.status}"

    class Meta:
        unique_together = (("enrollment","date","period"),)
        verbose_name = "سجل حضور طالب"
        verbose_name_plural = "سجلات حضور الطلبة"
