from django.db import models
from django.conf import settings
from backend.common.models import ShahaniaBaseModel
from backend.hr.models import Staff

# 1. The Committees Model
class QualityCommittee(ShahaniaBaseModel):
    """Represents a committee responsible for execution or evaluation."""
    COMMITTEE_TYPES = [
        ('executor', 'لجنة تنفيذ'),
        ('evaluator', 'لجنة مراجعة وتقييم'),
    ]
    name = models.CharField(max_length=200, verbose_name="اسم اللجنة")
    type = models.CharField(max_length=20, choices=COMMITTEE_TYPES, verbose_name="نوع اللجنة")
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="quality_committees",
        verbose_name="أعضاء اللجنة"
    )

    def __str__(self):
        return self.name

# 2. The Hierarchy: Domain -> Target -> Indicator
class QualityDomain(ShahaniaBaseModel):
    """Represents a quality rank/domain, e.g., 'Academic Achievement'."""
    name = models.CharField(max_length=255, unique=True, verbose_name="اسم المجال (Rank Name)")

    def __str__(self):
        return self.name

class QualityTarget(ShahaniaBaseModel):
    """A specific target within a domain."""
    domain = models.ForeignKey(QualityDomain, on_delete=models.CASCADE, related_name="targets", verbose_name="المجال")
    number = models.CharField(max_length=50, verbose_name="رقم الهدف")
    description = models.TextField(verbose_name="وصف الهدف")

    def __str__(self):
        return f"{self.number} - {self.description[:50]}"

class QualityIndicator(ShahaniaBaseModel):
    """A performance indicator to measure a target."""
    target = models.ForeignKey(QualityTarget, on_delete=models.CASCADE, related_name="indicators", verbose_name="الهدف")
    number = models.CharField(max_length=50, verbose_name="رقم المؤشر")
    description = models.TextField(verbose_name="وصف المؤشر")

    def __str__(self):
        return f"{self.number} - {self.description[:50]}"

# 3. The Core Operational Plan Item Model
class OperationalPlanItem(ShahaniaBaseModel):
    """
    This is the central model representing a single procedure/item in the operational plan.
    It maps directly to a row in the provided Excel file.
    """
    STATUS_CHOICES = [
        ('pending', 'لم تبدأ'),
        ('in_progress', 'قيد التنفيذ'),
        ('completed', 'مكتملة'),
        ('delayed', 'متأخرة'),
        ('cancelled', 'ملغاة'),
    ]

    # Hierarchy and Procedure
    indicator = models.ForeignKey(QualityIndicator, on_delete=models.CASCADE, related_name="plan_items", verbose_name="المؤشر")
    procedure_no = models.CharField(max_length=50, verbose_name="رقم الإجراء")
    procedure = models.TextField(verbose_name="الإجراء")
    
    # Responsibility
    executor = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name="executed_plan_items", verbose_name="المنفذ المباشر")
    executor_committee = models.ForeignKey(QualityCommittee, on_delete=models.SET_NULL, null=True, blank=True, related_name="executed_plans", verbose_name="لجنة التنفيذ")
    
    # Timeline
    date_range = models.CharField(max_length=100, verbose_name="النطاق الزمني (نصي)") # e.g., "May 2026"
    
    # Follow-up and Evidence
    follow_up = models.TextField(blank=True, null=True, verbose_name="إجراءات المتابعة")
    comments = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    evidence_type = models.CharField(max_length=200, blank=True, null=True, verbose_name="نوع الدليل")
    evidence_source_employee = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name="evidence_provided", verbose_name="مصدر الدليل (موظف)")
    evidence_source_file = models.FileField(upload_to='quality_evidence/', blank=True, null=True, verbose_name="ملف الدليل")
    
    # Evaluation
    evaluation = models.CharField(max_length=50, blank=True, null=True, verbose_name="التقييم")
    evaluation_notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات التقييم")
    evaluator_committee = models.ForeignKey(QualityCommittee, on_delete=models.SET_NULL, null=True, blank=True, related_name="evaluated_plans", verbose_name="لجنة التقييم")
    
    # Status
    operational_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="حالة التنفيذ")

    class Meta:
        verbose_name = "بند خطة تشغيلية"
        verbose_name_plural = "بنود الخطة التشغيلية"
        ordering = ['indicator__target__domain__name', 'indicator__target__number', 'indicator__number', 'procedure_no']

    def __str__(self):
        return self.procedure[:100]
