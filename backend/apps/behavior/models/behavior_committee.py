import uuid
from django.db import models


class BehaviorCommittee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    incident_id = models.UUIDField()  # FK → behavior_behaviorincident.id
    meeting_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "behavior_committee"
        managed = True
        unique_together = ("incident_id",)