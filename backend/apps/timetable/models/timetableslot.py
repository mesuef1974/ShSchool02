from django.db import models

class TimetableSlot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    day_of_week = models.SmallIntegerField()
    period = models.SmallIntegerField()
    class_room_id = models.UUIDField()
    room_id = models.UUIDField(null=True, blank=True)
    subject_id = models.UUIDField()
    teacher_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "timetable_timetableslot"
        managed = True
        unique_together = ("class_room_id", "day_of_week", "period")

