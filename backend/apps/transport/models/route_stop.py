from django.db import models

class TransportRouteStop(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route_id = models.UUIDField()
    seq = models.SmallIntegerField()
    name = models.CharField(max_length=120)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "transport_route_stop"
        managed = True
        unique_together = ("route_id", "seq")

