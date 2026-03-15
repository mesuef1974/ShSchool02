from django.contrib import admin
from ..models import Religion

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ar', 'name_en')
    search_fields = ('code', 'name_ar', 'name_en')

