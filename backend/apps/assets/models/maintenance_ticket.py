import uuid
from django.db import models
from .asset import Asset

class MaintenanceTicket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, verbose_name="الأصل", related_name="maintenance_tickets")
    type = models.CharField("نوع الصيانة", max_length=20, choices=[('preventive','وقائية'),('corrective','تصحيحية')])
    priority = models.CharField("الأولوية", max_length=20, default='normal')
    provider = models.CharField("المزود", max_length=150, blank=True, default="")
    opened_on = models.DateField("تاريخ الفتح", auto_now_add=True)
    closed_on = models.DateField("تاريخ الإغلاق", null=True, blank=True)
    notes = models.TextField("ملاحظات", blank=True, default="")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    deleted_at = models.DateTimeField("تاريخ الحذف", null=True, blank=True)
    row_version = models.IntegerField("إصدار الصف", default=1)

    class Meta:
        verbose_name = "تذكرة صيانة"
        verbose_name_plural = "تذاكر الصيانة"
        ordering = ["opened_on", "priority"]

    def __str__(self):
        return f"{self.asset} - {self.type}"

