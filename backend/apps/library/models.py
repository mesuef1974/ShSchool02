import uuid
from django.db import models
from apps.people.models import Student, Staff

class LibraryTitle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(max_length=20, blank=True, default="")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, blank=True, default="")

    def __str__(self):
        return f"{self.title} – {self.author}"

    class Meta:
        verbose_name = "عنوان كتاب"
        verbose_name_plural = "عناوين الكتب"

class LibraryCopy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default='available')

    def __str__(self):
        return f"نسخة: {self.title.title} – {self.barcode} ({self.status})"

    class Meta:
        verbose_name = "نسخة كتاب"
        verbose_name_plural = "نسخ الكتب"

class LibraryLoan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ⬅️ هنا كان الخطأ: يجب on_delete وليس "on delete"
    copy = models.ForeignKey(LibraryCopy, on_delete=models.PROTECT)
    borrower_student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    borrower_staff = models.ForeignKey(Staff,   null=True, blank=True, on_delete=models.SET_NULL)
    issued_on = models.DateField()
    due_on = models.DateField()
    returned_on = models.DateField(null=True, blank=True)

    def __str__(self):
        who = self.borrower_student or self.borrower_staff
        return f"إعارة: {self.copy.barcode} → {who}"

    class Meta:
        verbose_name = "إعارة"
        verbose_name_plural = "الإعارات"