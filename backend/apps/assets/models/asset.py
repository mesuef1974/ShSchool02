import uuid
from django.db import models
from apps.core.models import School, Room

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name="المدرسة", related_name="assets", null=True, blank=True)
    category = models.CharField("فئة الأصل", max_length=100)
    model = models.CharField("الموديل", max_length=150, blank=True, default="")
    serial_no = models.CharField("الرقم التسلسلي", max_length=150, blank=True, default="")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="الغرفة", related_name="assets", null=True, blank=True)
    notes = models.TextField("ملاحظات", blank=True, default="")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "أصل"
        verbose_name_plural = "الأصول"
        ordering = ["category", "model"]

    def __str__(self):
        return f"{self.category} - {self.model}"

