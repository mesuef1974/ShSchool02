import uuid
from django.db import models

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("اسم الاختبار", max_length=150)
    term_code = models.CharField("رمز الفصل", max_length=10)
    subject_id = models.UUIDField("معرف المادة")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "اختبار"
        verbose_name_plural = "الاختبارات"
        ordering = ["name"]

    def __str__(self):
        return self.name

