
import uuid
from django.db import models
from apps.core.models import School, Year, Subject, ClassRoom

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100, blank=True, default="")
    last_name_en = models.CharField(max_length=100, blank=True, default="")
    national_id = models.CharField(max_length=32, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=(("M","ذكر"),("F","أنثى")))
    phone = models.CharField(max_length=32, blank=True, default="")
    email = models.EmailField(blank=True, default="")

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلبة"

class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    phone = models.CharField(max_length=32)
    email = models.EmailField(blank=True, default="")

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

    class Meta:
        verbose_name = "ولي أمر"
        verbose_name_plural = "أولياء الأمور"

class StudentGuardian(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    relation = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} ← {self.guardian} ({self.relation})"

    class Meta:
        unique_together = (("student","guardian"),)
        verbose_name = "ربط طالب بولي الأمر"
        verbose_name_plural = "روابط الطلبة بأولياء الأمور"

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    job_title = models.CharField(max_length=120)
    email = models.EmailField(blank=True, default="")

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar} – {self.job_title}"

    class Meta:
        verbose_name = "موظف/معلم"
        verbose_name_plural = "الموظفون/المعلمون"

class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.teacher} ⇢ {self.class_room} ⇢ {self.subject}"

    class Meta:
        unique_together = (("teacher","class_room","subject"),)
        verbose_name = "تكليف تدريسي"
        verbose_name_plural = "التكاليف التدريسية"

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    grade = models.SmallIntegerField()
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.student} – {self.school.name_ar} – {self.year.label} – الصف {self.grade}"

    class Meta:
        unique_together = (("student","school","year","grade","class_room"),)
        verbose_name = "قيد طالب"
        verbose_name_plural = "قيود الطلبة"
