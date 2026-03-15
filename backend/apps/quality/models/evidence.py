from django.db import models

class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    opi_id = models.UUIDField(null=True, blank=True)
    kpi_code = models.CharField(max_length=60, null=True, blank=True)
    evidence_type = models.CharField(max_length=120, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

