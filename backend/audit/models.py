from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="الفاعل")
    action = models.CharField(max_length=16, verbose_name="الإجراء") # read/write/delete
    entity = models.CharField(max_length=64, verbose_name="الكيان")
    entity_id = models.UUIDField(verbose_name="معرّف الكيان")
    ts = models.DateTimeField(auto_now_add=True, verbose_name="التوقيت")
    meta = models.JSONField(null=True, blank=True, verbose_name="بيانات إضافية")

    class Meta:
        ordering = ['-ts']
        indexes = [
            models.Index(fields=['entity', 'entity_id', 'ts']),
        ]
