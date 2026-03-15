from django.contrib import admin
from ..models import QualityImprovementPlan

@admin.register(QualityImprovementPlan)
class QualityImprovementPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'year', 'goal', 'actions', 'owner', 'schedule', 'progress', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('owner', 'progress')

