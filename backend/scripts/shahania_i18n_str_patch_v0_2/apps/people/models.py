import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import School, Year, Subject, ClassRoom

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الطالب"))
    first_name_ar = models.CharField(max_length=100, verbose_name=_("الاسم الأول بالعربية"))
    last_name_ar = models.CharField(max_length=100, verbose_name=_("اسم العائلة بالعربية"))
    first_name_en = models.CharField(max_length=100, blank=True, default="", verbose_name=_("الاسم الأول بالإنجليزية"))
    last_name_en = models.CharField(max_length=100, blank=True, default="", verbose_name=_("اسم العائلة بالإنجليزية"))
    national_id = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("الرقم الوطني"))
    birth_date = models.DateField(verbose_name=_("تاريخ الميلاد"))
    gender = models.CharField(max_length=1, choices=(("M","ذكر"),("F","أنثى")), verbose_name=_("الجنس"))
    phone = models.CharField(max_length=32, blank=True, default="", verbose_name=_("رقم الهاتف"))
    email = models.EmailField(blank=True, default="", verbose_name=_("البريد الإلكتروني"))

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

    class Meta:
        verbose_name = _("طالب")
        verbose_name_plural = _("الطلبة")

class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف ولي الأمر"))
    first_name_ar = models.CharField(max_length=100, verbose_name=_("الاسم الأول بالعربية"))
    last_name_ar = models.CharField(max_length=100, verbose_name=_("اسم العائلة بالعربية"))
    phone = models.CharField(max_length=32, verbose_name=_("رقم الهاتف"))
    email = models.EmailField(blank=True, default="", verbose_name=_("البريد الإلكتروني"))

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"

    class Meta:
        verbose_name = _("ولي أمر")
        verbose_name_plural = _("أولياء الأمور")

class StudentGuardian(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("الطالب"))
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, verbose_name=_("ولي الأمر"))
    relation = models.CharField(max_length=30, verbose_name=_("العلاقة"))
    is_primary = models.BooleanField(default=False, verbose_name=_("ولي أساسي"))

    def __str__(self):
        return f"{self.student} ← {self.guardian} ({self.relation})"

    class Meta:
        unique_together = (("student","guardian"),)
        verbose_name = _("ربط طالب بولي الأمر")
        verbose_name_plural = _("روابط الطلبة بأولياء الأمور")

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الموظف"))
    first_name_ar = models.CharField(max_length=100, verbose_name=_("الاسم الأول بالعربية"))
    last_name_ar = models.CharField(max_length=100, verbose_name=_("اسم العائلة بالعربية"))
    job_title = models.CharField(max_length=120, verbose_name=_("المسمى الوظيفي"))
    email = models.EmailField(blank=True, default="", verbose_name=_("البريد الإلكتروني"))

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar} – {self.job_title}"

    class Meta:
        verbose_name = _("موظف/معلم")
        verbose_name_plural = _("الموظفون/المعلمون")

class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.PROTECT, verbose_name=_("المعلم"))
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT, verbose_name=_("الغرفة الصفية"))
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name=_("المادة"))

    def __str__(self):
        return f"{self.teacher} ⇢ {self.class_room} ⇢ {self.subject}"

    class Meta:
        unique_together = (("teacher","class_room","subject"),)
        verbose_name = _("تكليف تدريسي")
        verbose_name_plural = _("التكاليف التدريسية")

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف القيد"))
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name=_("الطالب"))
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name=_("المدرسة"))
    year = models.ForeignKey(Year, on_delete=models.PROTECT, verbose_name=_("السنة الدراسية"))
    grade = models.SmallIntegerField(verbose_name=_("الصف"))
    class_room = models.ForeignKey(ClassRoom, on_delete=models.PROTECT, verbose_name=_("الغرفة الصفية"))
    status = models.CharField(max_length=20, default='active', verbose_name=_("حالة القيد"))

    def __str__(self):
        return f"{self.student} – {self.school.name_ar} – {self.year.label} – الصف {self.grade}"

    class Meta:
        unique_together = (("student","school","year","grade","class_room"),)
        verbose_name = _("قيد طالب")
        verbose_name_plural = _("قيود الطلبة")
