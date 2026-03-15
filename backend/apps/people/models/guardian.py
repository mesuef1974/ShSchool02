import uuid
from django.db import models


class Guardian(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name_ar = models.CharField(max_length=100)
    last_name_ar = models.CharField(max_length=100)

    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)

    relation_to_student = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

    class Meta:
        db_table = "people_guardian"
        managed = True

    def __str__(self):
        return f"{self.first_name_ar} {self.last_name_ar}"