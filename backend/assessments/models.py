from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.academics.models import Subject, Term
from backend.students.models import Enrollment

class Exam(ShahaniaBaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="المادة")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name="الفصل")
    grade = models.CharField(max_length=16, verbose_name="الصف")
    is_makeup = models.BooleanField(default=False, verbose_name="اختبار تعويضي")

class ExamSession(ShahaniaBaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="الاختبار")
    session_date = models.DateField(verbose_name="تاريخ الجلسة")
    start_time = models.TimeField(verbose_name="وقت البدء")
    end_time = models.TimeField(verbose_name="وقت الانتهاء")

class ExamResult(ShahaniaBaseModel):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="القيد")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="الاختبار")
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="الدرجة")

    class Meta:
        unique_together = ('enrollment', 'exam')
