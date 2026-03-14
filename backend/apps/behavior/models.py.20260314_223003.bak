import uuid
from django.db import models
from apps.people.models import Student
class BehaviorIncident(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student=models.ForeignKey(Student, on_delete=models.PROTECT)
    date=models.DateField()
    period=models.SmallIntegerField(null=True, blank=True)
    place=models.CharField(max_length=120, blank=True, default='')
    category=models.CharField(max_length=80)
    description=models.TextField()
