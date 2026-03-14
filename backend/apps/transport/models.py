import uuid
from django.db import models
from apps.people.models import Student
class Route(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code=models.CharField(max_length=50, unique=True)
    capacity=models.IntegerField(default=0)
class StudentRider(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    route=models.ForeignKey(Route, on_delete=models.CASCADE)
    class Meta: unique_together=(('student','route'),)
