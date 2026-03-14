from django.db import models
from apps.core.models import School, Year, Subject, ClassRoom

class Student(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100, blank=True, default="")
    last_name_en = models.CharField(max_length=100, blank=True, default="")
    national_id = models.CharField(max_length=32, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M','ذكر'),('F','أنثى')))
    phone = models.CharField(max_length=32, blank=True, default="")
    email = models.EmailField(blank=True, default="")

class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    phone = models.CharField(max_length=32)
    email = models.EmailField(blank=True, default="")

class StudentGuardian(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    relation = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)
    class Meta:
        unique_together = (('student','guardian'),)

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    job_title = models.CharField(max_length=120)
    email = models.EmailField(blank=True, default="")

class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    class Meta:
        unique_together = (('teacher','class_room','subject'),)

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    grade = models.SmallIntegerField()
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='active')
    class Meta:
        unique_together = (('student','school','year','grade','class_room'),)
