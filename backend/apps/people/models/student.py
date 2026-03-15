import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100)
    last_name_en = models.CharField(max_length=100)

    national_id = models.CharField(max_length=32, null=True, blank=True)
    birth_date = models.DateField()

    gender = models.CharField(max_length=1)

    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)

    nationality_code = models.CharField(max_length=5, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    retention_until = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "people_student"
        managed = True

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"
