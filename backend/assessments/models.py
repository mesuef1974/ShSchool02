from django.db import models
from backend.common.models import BaseFormFields

class Exam(BaseFormFields):
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE)
    term = models.ForeignKey('students.Term', on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=32)  # midterm/final/quiz
    date = models.DateField()

class ExamSession(BaseFormFields):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    room = models.CharField(max_length=64)

class ExamResult(BaseFormFields):
    enrollment = models.ForeignKey('students.Enrollment', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=16)
