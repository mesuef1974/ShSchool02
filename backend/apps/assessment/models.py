import uuid
from django.db import models
from apps.core.models import Subject
from apps.people.models import Enrollment
class Exam(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=150)
    subject=models.ForeignKey(Subject, on_delete=models.PROTECT)
    term_code=models.CharField(max_length=10)
class ExamResult(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment=models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    score=models.DecimalField(max_digits=6, decimal_places=2)
    class Meta: unique_together=(('enrollment','exam'),)
class Appeal(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment=models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    reason=models.TextField()
    decision=models.TextField(blank=True, default='')
    class Meta: unique_together=(('enrollment','exam'),)
