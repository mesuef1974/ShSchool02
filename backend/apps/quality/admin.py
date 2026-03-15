from django.contrib import admin
from .models import QualityEvidence, ImprovementPlan, KpiSnapshot

@admin.register(QualityEvidence)
class QualityEvidenceAdmin(admin.ModelAdmin):
    list_display = ('domain', 'title', 'file_link')

@admin.register(ImprovementPlan)
class ImprovementPlanAdmin(admin.ModelAdmin):
    list_display = ('objective', 'owner', 'start_date', 'end_date', 'progress')

@admin.register(KpiSnapshot)
class KpiSnapshotAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'taken_on')

