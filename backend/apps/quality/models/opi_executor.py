from django.db import models

class QualityOpiExecutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    opi_id = models.UUIDField()
    executor_id = models.UUIDField()
    class Meta:
        unique_together = ("opi_id", "executor_id")

