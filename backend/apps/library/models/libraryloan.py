from django.db import models
from .librarycopy import LibraryCopy
from apps.people.models import Student, Staff

class LibraryLoan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    issued_on = models.DateField()
    due_on = models.DateField()
    returned_on = models.DateField(null=True, blank=True)
    borrower_staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    borrower_student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    copy = models.ForeignKey(LibraryCopy, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

