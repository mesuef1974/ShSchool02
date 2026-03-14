
import uuid
from django.db import models
from apps.people.models import Student

class ClinicVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField()
    reason = models.CharField(max_length=200)
    details_enc = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"عيادة: {self.student} – {self.date} – {self.reason}"

    class Meta:
        verbose_name = "زيارة عيادة"
        verbose_name_plural = "زيارات العيادة"
