import uuid
from django.db import models
from apps.people.models import Student,Staff
class LibraryTitle(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn=models.CharField(max_length=20, blank=True, default='')
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300, blank=True, default='')
class LibraryCopy(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.ForeignKey(LibraryTitle, on_delete=models.CASCADE)
    barcode=models.CharField(max_length=50, unique=True)
    status=models.CharField(max_length=20, default='available')
class LibraryLoan(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    copy=models.ForeignKey(LibraryCopy, on_delete=models.PROTECT)
    borrower_student=models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    borrower_staff=models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    issued_on=models.DateField(); due_on=models.DateField(); returned_on=models.DateField(null=True, blank=True)
