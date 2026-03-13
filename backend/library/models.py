from django.db import models
from backend.common.models import ShahaniaBaseModel

class LibraryTitle(ShahaniaBaseModel):
    isbn = models.CharField(max_length=32, unique=True, null=True, verbose_name="ISBN")
    title_ar = models.CharField(max_length=256, verbose_name="العنوان")
    author_ar = models.CharField(max_length=256, null=True, blank=True, verbose_name="المؤلف")

class LibraryCopy(ShahaniaBaseModel):
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE, verbose_name="الكتاب")
    copy_code = models.CharField(max_length=64, unique=True, verbose_name="رقم النسخة")

class LibraryLoan(ShahaniaBaseModel):
    copy = models.ForeignKey(LibraryCopy, on_delete=models.CASCADE, verbose_name="النسخة")
    borrower_id = models.UUIDField(verbose_name="المستعير") # Can be Student or Staff UUID
    loan_date = models.DateField(auto_now_add=True, verbose_name="تاريخ الإعارة")
    due_date = models.DateField(verbose_name="تاريخ الاستحقاق")
    return_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الإرجاع")
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="الغرامة")

class Reservation(ShahaniaBaseModel):
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE, verbose_name="الكتاب")
    requester_id = models.UUIDField(verbose_name="مقدم الطلب")
    reserved_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الحجز")
    fulfilled = models.BooleanField(default=False, verbose_name="تم التنفيذ")
