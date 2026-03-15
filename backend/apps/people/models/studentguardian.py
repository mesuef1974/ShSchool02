import uuid
from django.db import models


class StudentGuardian(models.Model):
    id = models.BigAutoField(primary_key=True)

    student_id = models.UUIDField()
    guardian_id = models.UUIDField()

    relation = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = "people_studentguardian"
        managed = True
        unique_together = ("student_id", "guardian_id")

    def __str__(self):
        return f"{self.student_id} ↔ {self.guardian_id} ({self.relation})"