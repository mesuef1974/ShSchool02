from django.db import models
from backend.common.models import BaseFormFields

class OffenseCode(BaseFormFields):
    code = models.CharField(max_length=16, unique=True)
    description = models.CharField(max_length=256)

class BehaviorIncident(BaseFormFields):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    offense_code = models.ForeignKey(OffenseCode, on_delete=models.CASCADE)
    reporter_id = models.UUIDField(null=True, blank=True)
    narrative = models.TextField(null=True, blank=True)
    evidence_ref = models.CharField(max_length=256, null=True, blank=True)

class BehaviorCommittee(BaseFormFields):
    incident = models.ForeignKey(BehaviorIncident, on_delete=models.CASCADE)
    decision = models.TextField()
    members = models.TextField()  # يمكن لاحقاً تحويلها لعلاقة مع Staff

class BehaviorSanction(BaseFormFields):
    incident = models.ForeignKey(BehaviorIncident, on_delete=models.CASCADE)
    sanction_type = models.CharField(max_length=64)
    details = models.TextField(null=True, blank=True)
