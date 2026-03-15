

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _


class Grade(models.Model):
    from django.utils.translation import gettext_lazy as _
    code = models.SmallIntegerField(
        primary_key=True,
        verbose_name=_("رمز الصف")
    )
    label_ar = models.CharField(
        _("اسم الصف"),
        max_length=50
    )
    label_en = models.CharField(
        _("اسم الصف (إنجليزي)"),
        max_length=50
    )

    def __str__(self):
        return self.label_ar

    class Meta:
        verbose_name = _("صف")
        verbose_name_plural = _("الصفوف")
        ordering = ["code"]