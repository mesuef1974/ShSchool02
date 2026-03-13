from django.db import models
from django.conf import settings
from backend.common.models import ShahaniaBaseModel

class Guardian(ShahaniaBaseModel):
    full_name_ar = models.CharField(max_length=128, verbose_name="اسم ولي الأمر")
    phone = models.CharField(max_length=32, verbose_name="رقم الهاتف")
    relation = models.CharField(max_length=32, null=True, blank=True, verbose_name="صلة القرابة")

    def __str__(self):
        return self.full_name_ar

class Student(ShahaniaBaseModel):
    national_id = models.CharField(max_length=32, unique=True, verbose_name="الرقم الشخصي")
    first_name_ar = models.CharField(max_length=64, verbose_name="الاسم الأول")
    last_name_ar = models.CharField(max_length=64, verbose_name="العائلة")
    dob = models.DateField(verbose_name="تاريخ الميلاد")
    nationality = models.CharField(max_length=64, null=True, blank=True, verbose_name="الجنسية")
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ولي الأمر")
    pdppl_consent = models.BooleanField(default=False, verbose_name="موافقة PDPPL")
    consent_ts = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الموافقة")

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

class Enrollment(ShahaniaBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    school_id = models.UUIDField(verbose_name="المدرسة")
    year_id = models.UUIDField(verbose_name="السنة")
    grade = models.CharField(max_length=16, verbose_name="الصف")
    section = models.CharField(max_length=8, null=True, blank=True, verbose_name="الشعبة")
    valid_from = models.DateField(verbose_name="ساري من")
    valid_to = models.DateField(null=True, blank=True, verbose_name="ساري إلى")

    class Meta:
        unique_together = ('student', 'school_id', 'year_id', 'grade', 'section')
    
    def __str__(self):
        return f"{self.student} - {self.grade}/{self.section}"
