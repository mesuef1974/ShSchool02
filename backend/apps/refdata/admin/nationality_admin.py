from django.contrib import admin
from ..models import Nationality

@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ar', 'name_en')
    search_fields = ('code', 'name_ar', 'name_en')

