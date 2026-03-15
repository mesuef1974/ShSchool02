
import uuid
from django.db import models
from .year import Year
from django.utils.translation import gettext_lazy as _


class Term(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    from django.utils.translation import gettext_lazy as _
    year = models.ForeignKey(
        Year,
        on_delete=models.PROTECT,
        verbose_name=_("العام الدراسي"),
        related_name="terms"
    )

    code = models.CharField(
        _("رمز الفصل"),
        max_length=10
    )  # مثال: T1, T2, T3

    start_date = models.DateField(_("تاريخ البداية"))
    end_date = models.DateField(_("تاريخ النهاية"))

    def __str__(self):
        return f"{self.code} – {self.year.label}"

    class Meta:
        verbose_name = _("فصل دراسي")
        verbose_name_plural = _("الفصول الدراسية")
        ordering = ["year__label", "code"]
        unique_together = ("year", "code")