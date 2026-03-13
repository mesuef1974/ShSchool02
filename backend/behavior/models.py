from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.students.models import Student

class OffenseCode(ShahaniaBaseModel):
    code = models.CharField(max_length=16, primary_key=True, verbose_name="رمز المخالفة")
    SEVERITY_CHOICES = [('MINOR', 'بسيطة'), ('MOD', 'متوسطة'), ('MAJOR', 'جسيمة')]
    severity = models.CharField(max_length=6, choices=SEVERITY_CHOICES, verbose_name="الخطورة")
    description = models.TextField(null=True, blank=True, verbose_name="الوصف")

class BehaviorIncident(ShahaniaBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الواقعة")
    offense_code = models.ForeignKey(OffenseCode, on_delete=models.PROTECT, verbose_name="رمز المخالفة")
    narrative = models.TextField(null=True, blank=True, verbose_name="تفاصيل الواقعة")
    evidence_ref = models.CharField(max_length=256, null=True, blank=True, verbose_name="مرجع الدليل")

class BehaviorCommittee(ShahaniaBaseModel):
    incident = models.OneToOneField(BehaviorIncident, on_delete=models.CASCADE, verbose_name="الواقعة")
    meeting_date = models.DateTimeField(verbose_name="تاريخ الاجتماع")
    decision = models.TextField(verbose_name="القرار")

class BehaviorSanction(ShahaniaBaseModel):
    incident = models.ForeignKey(BehaviorIncident, on_delete=models.CASCADE, verbose_name="الواقعة")
    sanction_type = models.CharField(max_length=32, verbose_name="نوع الإجراء")
    start_date = models.DateField(null=True, blank=True, verbose_name="تاريخ البدء")
    end_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الانتهاء")
