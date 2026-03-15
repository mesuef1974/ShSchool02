from django.db import models

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=150, unique=True)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

