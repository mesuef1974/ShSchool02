import uuid
from django.db import models


class BehaviorIncident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date = models.DateField()
    period = models.SmallIntegerField(null=True, blank=True)

    place = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    description = models.TextField()  # SENSITIVE

    student_id = models.UUIDField()  # FK → people_student.id

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    retention_until = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "behavior_behaviorincident"
        managed = True

    def __str__(self):
        return f"Incident {self.id} - {self.student_id}"