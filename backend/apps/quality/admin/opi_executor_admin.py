from django.contrib import admin
from ..models import QualityOpiExecutor

@admin.register(QualityOpiExecutor)
class QualityOpiExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'opi_id', 'executor_id')
    search_fields = ('opi_id', 'executor_id')

