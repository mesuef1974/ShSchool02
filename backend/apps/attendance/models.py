from django.db import models
from apps.people.models import Enrollment, Staff

class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date = models.DateField()
    period = models.SmallIntegerField()
    status = models.CharField(max_length=10, choices=(('present','حاضر'),('absent','غائب'),('late','متأخر'),('excused','معذور')))
    note = models.TextField(blank=True, default="")
    class Meta:
        unique_together = (('enrollment','date','period'),)

class StaffAttendance(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)
