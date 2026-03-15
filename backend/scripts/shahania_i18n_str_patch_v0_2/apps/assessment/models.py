import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import Subject
from apps.people.models import Enrollment

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الاختبار"))
    name = models.CharField(max_length=150, verbose_name=_("اسم الاختبار"))
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name=_("المادة"))
    term_code = models.CharField(max_length=10, verbose_name=_("رمز الفصل"))

    def __str__(self):
        return f"{self.name} – {self.subject} – {self.term_code}"

    class Meta:
        verbose_name = _("اختبار")
        verbose_name_plural = _("اختبارات")

class ExamSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الجلسة"))
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name=_("الاختبار"))
    date = models.DateField(verbose_name=_("تاريخ الجلسة"))
    start_time = models.TimeField(verbose_name=_("وقت البدء"))
    end_time = models.TimeField(verbose_name=_("وقت الانتهاء"))

    def __str__(self):
        return f"{self.exam} – {self.date} ({self.start_time}-{self.end_time})"

    class Meta:
        verbose_name = _("جلسة اختبار")
        verbose_name_plural = _("جلسات الاختبار")

class ExamResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف النتيجة"))
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name=_("قيد الطالب"))
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name=_("الاختبار"))
    score = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("الدرجة"))

    def __str__(self):
        return f"{self.enrollment.student} – {self.exam} = {self.score}"

    class Meta:
        unique_together = (("enrollment","exam"),)
        verbose_name = _("نتيجة اختبار")
        verbose_name_plural = _("نتائج الاختبارات")

class Appeal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف التظلّم"))
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name=_("قيد الطالب"))
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name=_("الاختبار"))
    reason = models.TextField(verbose_name=_("سبب التظلّم"))
    decision = models.TextField(blank=True, default="", verbose_name=_("قرار التظلّم"))

    def __str__(self):
        return f"تظلّم: {self.enrollment.student} – {self.exam}"

    class Meta:
        unique_together = (("enrollment","exam"),)
        verbose_name = _("تظلّم")
        verbose_name_plural = _("التظلّمات")
