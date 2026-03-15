import uuid
from django.db import models


class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    enrollment_id = models.UUIDField()   # FK → people_enrollment.id
    date = models.DateField()
    period = models.SmallIntegerField()  # 1..10

    status = models.CharField(max_length=10)  
    # allowed: present / absent / late / excused

    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "attendance_attendancerecord"
        managed = True
        unique_together = ("enrollment_id", "date", "period")

    def __str__(self):
        return f"{self.enrollment_id} - {self.date} (P{self.period})"