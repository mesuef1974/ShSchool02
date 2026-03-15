from django.db import models

class TransportRoute(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    supervisor_staff_id = models.UUIDField(null=True, blank=True)
    driver_name = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "transport_route"
        managed = True

