from django.db import models
from backend.common.models import BaseFormFields

class LibraryTitle(BaseFormFields):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    isbn = models.CharField(max_length=32, unique=True)

class LibraryCopy(BaseFormFields):
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE)
    copy_number = models.CharField(max_length=16)
    status = models.CharField(max_length=24)

class LibraryLoan(BaseFormFields):
    copy = models.ForeignKey(LibraryCopy, on_delete=models.CASCADE)
    borrower_id = models.UUIDField()
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
