from django.db import models

class TransportStudentRider(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route_id = models.UUIDField()
    student_id = models.UUIDField()
    pickup_stop_id = models.UUIDField(null=True, blank=True)
    dropoff_stop_id = models.UUIDField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "transport_studentrider"
        managed = True
        unique_together = ("student_id", "route_id")

