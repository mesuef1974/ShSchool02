from django.db import models
from backend.common.models import BaseFormFields

class ClinicVisit(BaseFormFields):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    visit_date = models.DateField()
    medical_note = models.BinaryField(null=True, blank=True)  # تشفير

class MedicationLog(BaseFormFields):
    clinic_visit = models.ForeignKey(ClinicVisit, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=128)
    dose = models.CharField(max_length=64)
    issued_at = models.DateTimeField()
