from django.contrib import admin
from ..models import QualityOperationalPlanItem

@admin.register(QualityOperationalPlanItem)
class QualityOperationalPlanItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'domain', 'status', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('year', 'domain', 'status')

