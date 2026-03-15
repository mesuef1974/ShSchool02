from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import Room

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الأصل"))
    name = models.CharField(max_length=200, verbose_name=_("اسم الأصل"))
    serial = models.CharField(max_length=100, blank=True, default="", verbose_name=_("الرقم التسلسلي"))
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("الغرفة"))

    class Meta:
        verbose_name = _("أصل")
        verbose_name_plural = _("الأصول")

class MaintenanceTicket(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف التذكرة"))
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, verbose_name=_("الأصل"))
    title = models.CharField(max_length=200, verbose_name=_("عنوان التذكرة"))
    description = models.TextField(verbose_name=_("الوصف"))
    status = models.CharField(max_length=20, default='open', verbose_name=_("الحالة"))

    class Meta:
        verbose_name = _("تذكرة صيانة")
        verbose_name_plural = _("تذاكر الصيانة")

class SafetyCertificate(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, verbose_name=_("معرّف الشهادة"))
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=_("الغرفة"))
    cert_type = models.CharField(max_length=120, verbose_name=_("نوع الشهادة"))
    valid_until = models.DateField(verbose_name=_("تاريخ الانتهاء"))
    file_link = models.CharField(max_length=500, blank=True, default="", verbose_name=_("رابط الملف"))

    class Meta:
        verbose_name = _("شهادة سلامة")
        verbose_name_plural = _("شهادات السلامة")
