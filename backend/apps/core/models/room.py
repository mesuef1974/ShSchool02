
import uuid
from django.db import models
from .school import School
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    from django.utils.translation import gettext_lazy as _
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name=_("المدرسة"),
        related_name="rooms"
    )

    code = models.CharField(
        _("رمز الغرفة"),
        max_length=50,
        unique=True
    )

    room_type = models.CharField(
        _("نوع الغرفة"),
        max_length=50
    )  # مثال: صف، مختبر، معمل، قاعة مناسبات

    capacity = models.PositiveIntegerField(
        _("السعة"),
        default=0
    )

    def __str__(self):
        return f"{self.code} – {self.school.name_ar}"

    class Meta:
        verbose_name = _("غرفة")
        verbose_name_plural = _("الغرف")
        ordering = ["code"]