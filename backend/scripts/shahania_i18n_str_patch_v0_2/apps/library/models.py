import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.people.models import Student, Staff

class LibraryTitle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف العنوان"))
    isbn = models.CharField(max_length=20, blank=True, default="", verbose_name=_("الرقم الدولي"))
    title = models.CharField(max_length=300, verbose_name=_("عنوان الكتاب"))
    author = models.CharField(max_length=300, blank=True, default="", verbose_name=_("المؤلف"))

    def __str__(self):
        return f"{self.title} – {self.author}"

    class Meta:
        verbose_name = _("عنوان كتاب")
        verbose_name_plural = _("عناوين الكتب")

class LibraryCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف النسخة"))
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE, verbose_name=_("عنوان الكتاب"))
    barcode = models.CharField(max_length=50, unique=True, verbose_name=_("الباركود"))
    status = models.CharField(max_length=20, default='available', verbose_name=_("الحالة"))

    def __str__(self):
        return f"نسخة: {self.title.title} – {self.barcode} ({self.status})"

    class Meta:
        verbose_name = _("نسخة كتاب")
        verbose_name_plural = _("نسخ الكتب")

class LibraryLoan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الإعارة"))
    copy = models.ForeignKey(LibraryCopy, on_delete=models.PROTECT, verbose_name=_("نسخة الكتاب"))
    borrower_student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("الطالب المستعير"))
    borrower_staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("الموظف المستعير"))
    issued_on = models.DateField(verbose_name=_("تاريخ الإعارة"))
    due_on = models.DateField(verbose_name=_("تاريخ الاستحقاق"))
    returned_on = models.DateField(null=True, blank=True, verbose_name=_("تاريخ الإرجاع"))

    def __str__(self):
        who = self.borrower_student or self.borrower_staff
        return f"إعارة: {self.copy.barcode} → {who}"

    class Meta:
        verbose_name = _("إعارة")
        verbose_name_plural = _("الإعارات")
