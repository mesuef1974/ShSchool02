import uuid
from django.db import models


class BehaviorSanction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    incident_id = models.UUIDField()  # FK → behavior_behaviorincident.id
    sanction_type = models.CharField(max_length=80)
    level = models.SmallIntegerField()
    decided_on = models.DateField()
    executed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "behavior_sanction"
        managed = True

    def __str__(self):
        return f"Sanction {self.incident_id} - {self.sanction_type}"