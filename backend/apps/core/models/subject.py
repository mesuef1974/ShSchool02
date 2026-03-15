import uuid
from django.db import models


class Subject(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name_ar = models.CharField(
        "اسم المادة",
        max_length=200
    )

    name_en = models.CharField(
        "اسم المادة (إنجليزي)",
        max_length=200,
        blank=True,
        default=""
    )

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "مادة"
        verbose_name_plural = "المواد"
        ordering = ["name_ar"]