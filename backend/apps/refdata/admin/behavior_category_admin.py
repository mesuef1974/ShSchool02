from django.contrib import admin
from ..models import BehaviorCategory

@admin.register(BehaviorCategory)
class BehaviorCategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ar')
    search_fields = ('code', 'name_ar')

