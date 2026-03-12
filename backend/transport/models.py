from django.db import models
from backend.common.models import BaseFormFields

class Bus(BaseFormFields):
    bus_number = models.CharField(max_length=16, unique=True)
    capacity = models.SmallIntegerField()

class Route(BaseFormFields):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=64)

class RouteStop(BaseFormFields):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=128)
    order = models.SmallIntegerField()

class StudentRider(BaseFormFields):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField()

class RideLog(BaseFormFields):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    rider = models.ForeignKey(StudentRider, on_delete=models.CASCADE)
    log_time = models.DateTimeField()
    status = models.CharField(max_length=24)
