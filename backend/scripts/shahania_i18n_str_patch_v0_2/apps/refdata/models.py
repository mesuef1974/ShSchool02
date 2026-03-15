from django.db import models
from django.utils.translation import gettext_lazy as _

class LookupNationality(models.Model):
    code = models.CharField(max_length=5, primary_key=True, verbose_name=_("رمز الجنسية"))
    name_ar = models.CharField(max_length=120, verbose_name=_("اسم الجنسية بالعربية"))
    name_en = models.CharField(max_length=120, blank=True, default="", verbose_name=_("اسم الجنسية بالإنجليزية"))

    def __str__(self):
        return f"{self.code} – {self.name_ar}"

    class Meta:
        verbose_name = _("جنسية")
        verbose_name_plural = _("الجنسيات")

class LookupAbsenceReason(models.Model):
    code = models.CharField(max_length=10, primary_key=True, verbose_name=_("رمز السبب"))
    name_ar = models.CharField(max_length=120, verbose_name=_("سبب الغياب"))

    def __str__(self):
        return f"{self.code} – {self.name_ar}"

    class Meta:
        verbose_name = _("سبب غياب")
        verbose_name_plural = _("أسباب الغياب")
