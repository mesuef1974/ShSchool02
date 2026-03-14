from django.db import models
from apps.people.models import Student

class Route(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField(default=0)

class RouteStop(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    seq = models.IntegerField()
    name = models.CharField(max_length=200)
    class Meta:
        unique_together = (('route','seq'),)

class StudentRider(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('student','route'),)

class RideLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    departed_at = models.TimeField(null=True, blank=True)
    arrived_at = models.TimeField(null=True, blank=True)
    class Meta:
        unique_together = (('route','date'),)

class DelayLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
