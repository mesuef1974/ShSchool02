
import uuid
from django.db import models
from apps.core.models import Subject
from apps.people.models import Enrollment

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    term_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} – {self.subject} – {self.term_code}"

    class Meta:
        verbose_name = "اختبار"
        verbose_name_plural = "اختبارات"

class ExamSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.exam} – {self.date} ({self.start_time}-{self.end_time})"

    class Meta:
        verbose_name = "جلسة اختبار"
        verbose_name_plural = "جلسات الاختبار"

class ExamResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.enrollment.student} – {self.exam} = {self.score}"

    class Meta:
        unique_together = (("enrollment","exam"),)
        verbose_name = "نتيجة اختبار"
        verbose_name_plural = "نتائج الاختبارات"

class Appeal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    reason = models.TextField()
    decision = models.TextField(blank=True, default="")

    def __str__(self):
        return f"تظلّم: {self.enrollment.student} – {self.exam}"

    class Meta:
        unique_together = (("enrollment","exam"),)
        verbose_name = "تظلّم"
        verbose_name_plural = "التظلّمات"
