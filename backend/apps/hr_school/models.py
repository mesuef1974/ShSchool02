from django.db import models
from apps.people.models import Staff

class StaffProfile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    department = models.CharField(max_length=120, blank=True, default="")

class LeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')

class PerformanceReview(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    period_label = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, default="")
