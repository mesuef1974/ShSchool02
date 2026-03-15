import uuid
from django.db import models


class TeachingAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)

    class_room_id = models.UUIDField()  # FK → core_classroom.id
    subject_id = models.UUIDField()     # FK → core_subject.id
    teacher_id = models.UUIDField()     # FK → people_staff.id

    class Meta:
        db_table = "people_teachingassignment"
        managed = True
        unique_together = ("teacher_id", "class_room_id", "subject_id")

    def __str__(self):
        return f"{self.teacher_id} teaches {self.subject_id} in {self.class_room_id}"