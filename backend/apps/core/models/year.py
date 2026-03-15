
import uuid
from django.db import models
from .school import School
from django.utils.translation import gettext_lazy as _


class Year(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    from django.utils.translation import gettext_lazy as _
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name=_("المدرسة"),
        related_name="years"
    )

    label = models.CharField(
        _("العام الدراسي"),
        max_length=20    # مثال: 2025-2026
    )

    start_date = models.DateField(_("تاريخ البداية"))
    end_date = models.DateField(_("تاريخ النهاية"))

    def __str__(self):
        return f"{self.label} - {self.school.name_ar}"

    class Meta:
        verbose_name = _("عام دراسي")
        verbose_name_plural = _("الأعوام الدراسية")
        ordering = ["label"]   # ← ← ← هذا السطر كان ناقص
        unique_together = ("school", "label")