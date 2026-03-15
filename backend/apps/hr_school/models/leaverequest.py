from django.db import models
from apps.people.models import Staff

class LeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='pending')
    notes = models.TextField(blank=True, default="")
    # ...existing code...

