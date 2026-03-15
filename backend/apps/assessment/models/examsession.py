import uuid
from django.db import models
from .exam import Exam

class ExamSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, verbose_name="الاختبار", related_name="sessions")
    room_id = models.UUIDField("معرف الغرفة")
    date = models.DateField("تاريخ الجلسة")
    start_time = models.TimeField("وقت البداية")
    end_time = models.TimeField("وقت النهاية")
    invigilator_staff_id = models.UUIDField("معرف المراقب", null=True, blank=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "جلسة اختبار"
        verbose_name_plural = "جلسات الاختبار"
        unique_together = ("exam", "room_id", "date", "start_time")
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.exam.name} - {self.date}"

