from django.db import models
from apps.core.models import ClassRoom, Subject, Room
from apps.people.models import Staff

class TimetableRule(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)

class TimetableSlot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    day_of_week = models.SmallIntegerField()
    period = models.SmallIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    class Meta:
        unique_together = (('class_room','day_of_week','period'),)
