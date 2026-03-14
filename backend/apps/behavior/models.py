from django.db import models
from apps.people.models import Student

class BehaviorIncident(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField()
    period = models.SmallIntegerField(null=True, blank=True)
    place = models.CharField(max_length=120, blank=True, default="")
    category = models.CharField(max_length=80)
    description = models.TextField()

class BehaviorCommittee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    incident = models.OneToOneField(BehaviorIncident, on_delete=models.CASCADE)
    members = models.TextField()  # أسماء الأعضاء
    minutes = models.TextField(blank=True, default="")

class BehaviorSanction(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    incident = models.ForeignKey(BehaviorIncident, on_delete=models.CASCADE)
    sanction_type = models.CharField(max_length=120)
    notes = models.TextField(blank=True, default="")
