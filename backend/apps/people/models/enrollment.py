import uuid
from django.db import models


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    grade = models.SmallIntegerField()  # FK → core_grade.code
    status = models.CharField(max_length=20)  # active / transferred / graduated / withdrawn

    class_room_id = models.UUIDField()  # FK → core_classroom.id
    school_id = models.UUIDField()      # FK → core_school.id
    year_id = models.UUIDField()        # FK → core_year.id
    student_id = models.UUIDField()     # FK → people_student.id

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "people_enrollment"
        managed = True
        unique_together = ("student_id", "school_id", "year_id", "grade", "class_room_id")

    def __str__(self):
        return f"Enrollment {self.student_id} - {self.grade}"