from django.db import models

class TransportDelayLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    ride_id = models.UUIDField()
    minutes_late = models.SmallIntegerField()
    reason = models.CharField(max_length=120, null=True, blank=True)
    notified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "transport_delay_log"
        managed = True

