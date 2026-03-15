from django.db import models

class TransportRideLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route_id = models.UUIDField()
    date = models.DateField()
    departed_at = models.TimeField(null=True, blank=True)
    arrived_at = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "transport_ride_log"
        managed = True
        unique_together = ("route_id", "date")

