from django.contrib import admin
from ..models import QualityPlanExecutor

@admin.register(QualityPlanExecutor)
class QualityPlanExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title', 'staff', 'is_active', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('name', 'job_title')

