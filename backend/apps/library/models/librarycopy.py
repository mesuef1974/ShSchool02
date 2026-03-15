from django.db import models
from .librarytitle import LibraryTitle

class LibraryCopy(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    barcode = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20)
    title = models.ForeignKey(LibraryTitle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

