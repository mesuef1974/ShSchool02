

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    from django.utils.translation import gettext_lazy as _
    name_ar = models.CharField(
        _("اسم المدرسة"),
        max_length=200
    )

    name_en = models.CharField(
        _("اسم المدرسة (إنجليزي)"),
        max_length=200,
        blank=True,
        default=""
    )

    moehe_code = models.CharField(
        _("كود الوزارة"),
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = _("مدرسة")
        verbose_name_plural = _("المدارس")
