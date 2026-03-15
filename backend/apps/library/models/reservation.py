from django.db import models
from .librarycopy import LibraryCopy
from apps.people.models import Student, Staff

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    copy = models.ForeignKey(LibraryCopy, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    reserved_on = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateTimeField()
    fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        unique_together = ("copy", "student", "staff", "fulfilled")

