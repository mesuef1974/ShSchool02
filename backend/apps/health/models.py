import uuid
from django.db import models
from apps.people.models import Student
class ClinicVisit(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student=models.ForeignKey(Student, on_delete=models.PROTECT)
    date=models.DateField()
    reason=models.CharField(max_length=200)
    details_enc=models.BinaryField(null=True, blank=True)
