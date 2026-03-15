import uuid
from django.db import models
from .school import School


class Room(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name="المدرسة",
        related_name="rooms"
    )

    code = models.CharField(
        "رمز الغرفة",
        max_length=50,
        unique=True
    )

    room_type = models.CharField(
        "نوع الغرفة",
        max_length=50
    )  # مثال: صف، مختبر، معمل، قاعة مناسبات

    capacity = models.PositiveIntegerField(
        "السعة",
        default=0
    )

    def __str__(self):
        return f"{self.code} – {self.school.name_ar}"

    class Meta:
        verbose_name = "غرفة"
        verbose_name_plural = "الغرف"
        ordering = ["code"]