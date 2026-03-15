from django.db import models
from apps.core.models import School, Year

class QualityKpiSnapshot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    kpi_code = models.CharField(max_length=60)
    kpi_label = models.CharField(max_length=200)
    snapshot_on = models.DateField()
    value_numeric = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    value_text = models.CharField(max_length=200, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

