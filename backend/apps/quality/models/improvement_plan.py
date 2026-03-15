from django.db import models
from apps.core.models import School, Year

class QualityImprovementPlan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    goal = models.TextField()
    actions = models.TextField()
    owner = models.CharField(max_length=150)
    schedule = models.TextField(null=True, blank=True)
    progress = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

