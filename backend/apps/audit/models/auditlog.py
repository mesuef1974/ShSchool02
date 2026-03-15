from django.db import models

class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=120)
    record_id = models.CharField(max_length=64)
    actor_user = models.CharField(max_length=120)
    action = models.CharField(max_length=10)
    old_values = models.JSONField(null=True, blank=True)
    new_values = models.JSONField(null=True, blank=True)
    ip = models.CharField(max_length=50, blank=True, default="")
    ua = models.CharField(max_length=200, blank=True, default="")
    ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "سجل تدقيق"
        verbose_name_plural = "سجلات التدقيق"
        ordering = ["ts"]

    def __str__(self):
        return f"{self.table_name} - {self.action}"

