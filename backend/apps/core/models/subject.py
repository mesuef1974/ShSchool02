

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    from django.utils.translation import gettext_lazy as _
    name_ar = models.CharField(
        _("اسم المادة"),
        max_length=200
    )

    name_en = models.CharField(
        _("اسم المادة (إنجليزي)"),
        max_length=200,
        blank=True,
        default=""
    )

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = _("مادة")
        verbose_name_plural = _("المواد")
        ordering = ["name_ar"]