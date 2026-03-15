import uuid
from django.db import models
from .exam import Exam

class ExamResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.DecimalField("الدرجة", max_digits=6, decimal_places=2)
    enrollment_id = models.UUIDField("معرف التسجيل")
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, verbose_name="الاختبار", related_name="results")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "نتيجة اختبار"
        verbose_name_plural = "نتائج الاختبارات"
        unique_together = ("enrollment_id", "exam")
        ordering = ["exam", "enrollment_id"]

    def __str__(self):
        return f"{self.exam.name} - {self.score}"

