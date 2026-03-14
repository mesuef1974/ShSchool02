
from django.db import models

class LookupNationality(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120, blank=True, default="")

    def __str__(self):
        return f"{self.code} – {self.name_ar}"

    class Meta:
        verbose_name = "جنسية"
        verbose_name_plural = "الجنسيات"

class LookupAbsenceReason(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name_ar = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.code} – {self.name_ar}"

    class Meta:
        verbose_name = "سبب غياب"
        verbose_name_plural = "أسباب الغياب"
