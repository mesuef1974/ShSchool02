from django.db import models
from backend.common.models import BaseFormFields

class School(BaseFormFields):
    name_ar = models.CharField(max_length=256)
    moe_code = models.CharField(max_length=32, unique=True, null=True, blank=True)
    level = models.CharField(max_length=32, null=True, blank=True)  # preparatory/secondary

class AcademicYear(BaseFormFields):
    code = models.CharField(max_length=9, unique=True)  # e.g., 2025-2026

class Term(BaseFormFields):
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='terms')
    code = models.CharField(max_length=8)

    class Meta:
        unique_together = ('year', 'code')

class Guardian(BaseFormFields):
    full_name_ar = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    relation = models.CharField(max_length=32, null=True, blank=True)

class Student(BaseFormFields):
    national_id = models.CharField(max_length=32, unique=True)
    first_name_ar = models.CharField(max_length=64)
    last_name_ar = models.CharField(max_length=64)
    dob = models.DateField()
    nationality = models.CharField(max_length=64, null=True, blank=True)
    guardian = models.ForeignKey(Guardian, null=True, blank=True, on_delete=models.SET_NULL)
    pdppl_guardian_consent = models.BooleanField(default=False)
    consent_ts = models.DateTimeField(null=True, blank=True)

class Enrollment(BaseFormFields):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    grade = models.CharField(max_length=16)
    section = models.CharField(max_length=8, null=True, blank=True)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'school', 'year', 'grade', 'section')
