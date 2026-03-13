from django.db import models
from django.conf import settings
import uuid
from backend.common.models import ShahaniaBaseModel

class School(ShahaniaBaseModel):
    name_ar = models.CharField(max_length=256, verbose_name="اسم المدرسة (ع)")
    moe_code = models.CharField(max_length=32, unique=True, null=True, verbose_name="رمز الوزارة")
    LEVEL_CHOICES = [
        ('primary', 'ابتدائي'),
        ('preparatory', 'إعدادي'),
        ('secondary', 'ثانوي'),
        ('grouped', 'مجمعة')
    ]
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, verbose_name="المرحلة")

    def __str__(self):
        return self.name_ar

class AcademicYear(ShahaniaBaseModel):
    code = models.CharField(max_length=9, unique=True, verbose_name="العام الأكاديمي") # 2025-2026
    def __str__(self):
        return self.code

class Term(ShahaniaBaseModel):
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name="السنة", related_name="terms")
    code = models.CharField(max_length=8, verbose_name="الفصل")
    def __str__(self):
        return f"{self.year} - {self.code}"
    class Meta:
        unique_together = ('year', 'code')

class Subject(ShahaniaBaseModel):
    code = models.CharField(max_length=32, unique=True, verbose_name="رمز المادة")
    name_ar = models.CharField(max_length=128, verbose_name="اسم المادة")

class ClassRoom(ShahaniaBaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="المدرسة")
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name="السنة الأكاديمية", related_name="classrooms")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name="الفصل الدراسي", related_name="classrooms", null=True, blank=True)
    grade = models.CharField(max_length=16, verbose_name="الصف")
    section = models.CharField(max_length=8, verbose_name="الشعبة")
    capacity = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        unique_together = ('school', 'year', 'term', 'grade', 'section')

class Teacher(ShahaniaBaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="المستخدم")
    staff_code = models.CharField(max_length=32, unique=True, null=True, verbose_name="رقم الموظف")

class TeachingAssignment(ShahaniaBaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="المعلم")
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="الفصل")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="المادة")
    weekly_load = models.SmallIntegerField(null=True, blank=True, verbose_name="النصاب الأسبوعي")

    class Meta:
        unique_together = ('teacher', 'class_room', 'subject')
