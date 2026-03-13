from django.db import models
from django.conf import settings
from backend.common.models import ShahaniaBaseModel

class Staff(ShahaniaBaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="المستخدم")
    job_title = models.CharField(max_length=128, null=True, blank=True, verbose_name="المسمى الوظيفي")
    hire_date = models.DateField(null=True, blank=True, verbose_name="تاريخ التعيين")

class StaffAttendance(ShahaniaBaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="الموظف")
    date = models.DateField(verbose_name="التاريخ")
    check_in = models.TimeField(null=True, blank=True, verbose_name="وقت الدخول")
    check_out = models.TimeField(null=True, blank=True, verbose_name="وقت الخروج")
    STATUS_CHOICES = [('present', 'حضور'), ('absent', 'غياب'), ('leave', 'إجازة')]
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, verbose_name="الحالة")

    class Meta:
        unique_together = ('staff', 'date')

class LeaveRequest(ShahaniaBaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="الموظف")
    leave_type = models.CharField(max_length=24, verbose_name="نوع الإجازة")
    date_from = models.DateField(verbose_name="من")
    date_to = models.DateField(verbose_name="إلى")
    balance_before = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="الرصيد قبل")
    status = models.CharField(max_length=16, default='pending', verbose_name="الحالة")

class PerformanceReview(ShahaniaBaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="الموظف")
    kpi_scores = models.JSONField(verbose_name="درجات الأداء")
    overall = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="التقييم العام")
