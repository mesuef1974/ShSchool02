from django.db import models

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    school = models.ForeignKey('core.School', on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=200, default="عنوان افتراضي")
    content = models.TextField(default="محتوى افتراضي")
    start_on = models.DateTimeField(null=True, blank=True)
    end_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default='2026-03-15T00:00:00Z')
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
