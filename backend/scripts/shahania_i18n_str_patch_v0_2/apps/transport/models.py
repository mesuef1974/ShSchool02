
import uuid
from django.db import models
from apps.people.models import Student

class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"مسار {self.code} (سعة {self.capacity})"

    class Meta:
        verbose_name = "مسار نقل"
        verbose_name_plural = "مسارات النقل"

class RouteStop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    seq = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.route.code} – محطة {self.seq}: {self.name}"

    class Meta:
        unique_together = (("route","seq"),)
        verbose_name = "محطة"
        verbose_name_plural = "محطات"

class StudentRider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} ↔ {self.route.code}"

    class Meta:
        unique_together = (("student","route"),)
        verbose_name = "مستقل حافلة"
        verbose_name_plural = "مستقلو الحافلات"
