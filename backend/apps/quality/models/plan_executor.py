from django.db import models
from apps.people.models import Staff

class QualityPlanExecutor(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=150, null=True, blank=True)
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

