from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.students.models import Student

class NoticeTemplate(ShahaniaBaseModel):
    code = models.CharField(max_length=32, unique=True, verbose_name="رمز القالب")
    channel = models.CharField(max_length=16, verbose_name="القناة")
    subject = models.CharField(max_length=128, null=True, blank=True, verbose_name="الموضوع")
    body = models.TextField(verbose_name="نص الرسالة")

class Notice(ShahaniaBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    template = models.ForeignKey(NoticeTemplate, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="القالب")
    notice_type = models.CharField(max_length=32, verbose_name="نوع الإشعار")
    channel = models.CharField(max_length=32, verbose_name="القناة")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")
    payload = models.JSONField(null=True, blank=True, verbose_name="البيانات")
