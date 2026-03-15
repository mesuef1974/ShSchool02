from django.db import models
from apps.people.models import Student

class MedicationLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField()
    medicine = models.CharField(max_length=120)
    dose = models.CharField(max_length=60)
    notes_enc = models.BinaryField(null=True, blank=True)

