from django.db import models
from django.conf import settings
import uuid

class ShahaniaBaseModel(models.Model):
    """
    Abstract base model that implements the 'StandardFields' from the Excel catalog.
    All operational models in the system should inherit from this.
    """
    # Standard Fields as per Excel Sheet 'StandardFields'
    form_uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, null=True, blank=True, verbose_name="معرّف السجل")
    
    # Context Fields
    school_id = models.UUIDField(verbose_name="معرّف المدرسة", null=True, blank=True) # Can be FK to School model later
    academic_year = models.CharField(max_length=9, null=True, blank=True, verbose_name="السنة الأكاديمية") # e.g. 2025-2026
    term = models.CharField(max_length=8, null=True, blank=True, verbose_name="الفصل الدراسي") # e.g. T1, T2
    
    # Audit Fields
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تعديل")
    
    # Status
    STATUS_CHOICES = [
        ('draft', 'مسودة'),
        ('final', 'نهائي'),
        ('archived', 'مؤرشف'),
    ]
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='draft', verbose_name="حالة السجل")

    class Meta:
        abstract = True
        ordering = ['-created_at']
