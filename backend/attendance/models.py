from django.db import models
from backend.common.models import BaseFormFields

class AttendanceRecord(BaseFormFields):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=24)  # present/absent/late
    arrival_time = models.TimeField(null=True, blank=True)
    minutes_late = models.SmallIntegerField(null=True, blank=True)
    action = models.CharField(max_length=64, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    guardian_id_doc = models.CharField(max_length=64, null=True, blank=True)
    evidence_doc_ref = models.CharField(max_length=256, null=True, blank=True)
