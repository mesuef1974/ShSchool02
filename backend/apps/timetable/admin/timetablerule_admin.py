from django.contrib import admin
from ..models import TimetableRule

@admin.register(TimetableRule)
class TimetableRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('name',)

