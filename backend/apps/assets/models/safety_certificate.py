import uuid
from django.db import models
from apps.core.models import School, Room

class SafetyCertificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name="المدرسة", related_name="safety_certificates", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="الغرفة", related_name="safety_certificates", null=True, blank=True)
    certificate_type = models.CharField("نوع الشهادة", max_length=120)
    file_link = models.TextField("رابط الملف", blank=True, default="")
    valid_until = models.DateField("تاريخ الانتهاء", null=True, blank=True)
    notes = models.TextField("ملاحظات", blank=True, default="")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "شهادة سلامة"
        verbose_name_plural = "شهادات السلامة"
        ordering = ["certificate_type", "valid_until"]

    def __str__(self):
        return f"{self.certificate_type} - {self.room}"

