import uuid
from django.db import models
from .school import School
from .year import Year
from .grade import Grade

from django.utils.translation import gettext_lazy as _


class ClassRoom(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name=_("المدرسة"),
        related_name="classrooms"
    )

    year = models.ForeignKey(
        Year,
        on_delete=models.PROTECT,
        verbose_name=_("العام الدراسي"),
        related_name="classrooms"
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        verbose_name=_("الصف"),
        related_name="classrooms"
    )

    section = models.CharField(
        _("الشعبة"),
        max_length=10
    )

    def __str__(self):
        return f"{self.grade.label_ar} / {self.section} – {self.school.name_ar}"

    class Meta:
        verbose_name = _("شعبة صف")
        verbose_name_plural = _("شُعب الصفوف")
        unique_together = ("school", "year", "grade", "section")
        ordering = ["grade__code", "section"]