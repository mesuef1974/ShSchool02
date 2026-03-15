import uuid
from django.db import models


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)

    job_title = models.CharField(max_length=120)

    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=32, null=True, blank=True)

    department = models.CharField(max_length=120, null=True, blank=True)

    status = models.CharField(max_length=30, default="active")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "people_staff"
        managed = True

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"