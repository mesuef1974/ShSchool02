from django.db import models

class LibraryTitle(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    isbn = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

