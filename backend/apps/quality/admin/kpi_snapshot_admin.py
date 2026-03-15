from django.contrib import admin
from ..models import QualityKpiSnapshot

@admin.register(QualityKpiSnapshot)
class QualityKpiSnapshotAdmin(admin.ModelAdmin):
    list_display = ('id', 'kpi_code', 'kpi_label', 'snapshot_on', 'value_numeric', 'value_text', 'school', 'year', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('kpi_code', 'kpi_label')

