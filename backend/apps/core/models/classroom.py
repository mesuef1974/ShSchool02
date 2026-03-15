import uuid
from django.db import models
from .school import School
from .year import Year
from .grade import Grade


class ClassRoom(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name="المدرسة",
        related_name="classrooms"
    )

    year = models.ForeignKey(
        Year,
        on_delete=models.PROTECT,
        verbose_name="العام الدراسي",
        related_name="classrooms"
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        verbose_name="الصف",
        related_name="classrooms"
    )

    section = models.CharField(
        "الشعبة",
        max_length=10
    )

    def __str__(self):
        return f"{self.grade.label_ar} / {self.section} – {self.school.name_ar}"

    class Meta:
        verbose_name = "شعبة صف"
        verbose_name_plural = "شُعب الصفوف"
        unique_together = ("school", "year", "grade", "section")
        ordering = ["grade__code", "section"]