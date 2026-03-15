from django.contrib import admin
from ..models import QualityEvidence

@admin.register(QualityEvidence)
class QualityEvidenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'opi_id', 'kpi_code', 'evidence_type', 'link', 'notes', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('kpi_code', 'evidence_type')

