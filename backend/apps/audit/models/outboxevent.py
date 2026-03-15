from django.db import models

class OutboxEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=120)
    payload = models.JSONField()
    status = models.CharField(max_length=20, default='pending')
    ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "حدث صادر"
        verbose_name_plural = "الأحداث الصادرة"
        ordering = ["ts"]

    def __str__(self):
        return f"{self.event_type} - {self.status}"

