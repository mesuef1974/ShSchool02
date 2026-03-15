
import uuid
from django.db import models


class School(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name_ar = models.CharField(
        "اسم المدرسة",
        max_length=200
    )

    name_en = models.CharField(
        "اسم المدرسة (إنجليزي)",
        max_length=200,
        blank=True,
        default=""
    )

    moehe_code = models.CharField(
        "كود الوزارة",
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "مدرسة"
        verbose_name_plural = "المدارس"
