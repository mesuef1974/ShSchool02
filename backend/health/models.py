from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.students.models import Student

class ClinicVisit(ShahaniaBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    visited_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الزيارة")
    
    # Sensitive Data (Stored as BYTEA/BinaryField for Application-Level Encryption)
    complaint_enc = models.BinaryField(null=True, blank=True, verbose_name="الشكوى (مشفّر)")
    diagnosis_enc = models.BinaryField(null=True, blank=True, verbose_name="التشخيص (مشفّر)")
    action_taken_enc = models.BinaryField(null=True, blank=True, verbose_name="الإجراء (مشفّر)")
    
    vitals = models.JSONField(null=True, blank=True, verbose_name="العلامات الحيوية")
    retention_until = models.DateField(null=True, blank=True, verbose_name="تاريخ الاحتفاظ")

class MedicationLog(ShahaniaBaseModel):
    visit = models.ForeignKey(ClinicVisit, on_delete=models.CASCADE, verbose_name="الزيارة")
    med_name_enc = models.BinaryField(verbose_name="اسم الدواء (مشفّر)")
    dose = models.CharField(max_length=32, null=True, blank=True, verbose_name="الجرعة")
    administered_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإعطاء")
