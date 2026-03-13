from django.db import models
from backend.common.models import ShahaniaBaseModel

class AttendanceRecord(ShahaniaBaseModel):
    # We need to import Enrollment inside the class or use string reference to avoid circular import if possible,
    # but since Enrollment is in 'students', we can import it.
    enrollment = models.ForeignKey('students.Enrollment', on_delete=models.CASCADE, verbose_name="قيد الطالب")
    date = models.DateField(verbose_name="التاريخ")
    period = models.SmallIntegerField(null=True, blank=True, verbose_name="الحصة")
    
    STATUS_CHOICES = [
        ('P', 'حضور'), 
        ('A', 'غياب'), 
        ('E', 'عذر'), 
        ('L', 'تأخر'), 
        ('ED', 'انصراف مبكر')
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="الحالة")
    reason_code = models.CharField(max_length=32, null=True, blank=True, verbose_name="رمز السبب")
    archived = models.BooleanField(default=False, verbose_name="مؤرشف")

    class Meta:
        unique_together = ('enrollment', 'date', 'period')
        verbose_name = "سجل الحضور"
        verbose_name_plural = "سجلات الحضور"
