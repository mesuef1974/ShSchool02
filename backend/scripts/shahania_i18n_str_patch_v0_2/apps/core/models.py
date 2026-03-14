
import uuid
from django.db import models

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True, default="")
    moehe_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name_ar} ({self.moehe_code})"

    class Meta:
        verbose_name = "مدرسة"
        verbose_name_plural = "المدارس"

class Year(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    label = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.school.name_ar} – {self.label}"

    class Meta:
        verbose_name = "عام دراسي"
        verbose_name_plural = "الأعوام الدراسية"

class Term(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.year.label} / الفصل {self.code}"

    class Meta:
        unique_together = (("year","code"),)
        verbose_name = "فصل دراسي"
        verbose_name_plural = "الفصول الدراسية"

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "مادة"
        verbose_name_plural = "المواد"

class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    grade = models.SmallIntegerField()
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.school.name_ar} – {self.year.label} – الصف {self.grade} / الشعبة {self.section}"

    class Meta:
        unique_together = (("school","year","grade","section"),)
        verbose_name = "شعبة صف"
        verbose_name_plural = "شُعب الصفوف"

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.school.name_ar} – {self.code} ({self.room_type})"

    class Meta:
        verbose_name = "قاعة/غرفة"
        verbose_name_plural = "القاعات/الغرف"
