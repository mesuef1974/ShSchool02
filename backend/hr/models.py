from django.db import models
from backend.common.models import BaseFormFields

class Staff(BaseFormFields):
    full_name_ar = models.CharField(max_length=128)
    position = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, null=True, blank=True)

class StaffAttendance(BaseFormFields):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=24)

class LeaveRequest(BaseFormFields):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=32)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField(null=True, blank=True)

class DisciplinaryAction(BaseFormFields):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=64)
    details = models.TextField(null=True, blank=True)

class PerformanceReview(BaseFormFields):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    reviewer_id = models.UUIDField()
    review_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
