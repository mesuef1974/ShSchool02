from django.db import models


class Grade(models.Model):
    code = models.SmallIntegerField(
        primary_key=True,
        verbose_name="رمز الصف"
    )
    label_ar = models.CharField(
        "اسم الصف",
        max_length=50
    )
    label_en = models.CharField(
        "اسم الصف (إنجليزي)",
        max_length=50
    )

    def __str__(self):
        return self.label_ar

    class Meta:
        verbose_name = "صف"
        verbose_name_plural = "الصفوف"
        ordering = ["code"]