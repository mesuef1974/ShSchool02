
from django.contrib import admin
from .models import BehaviorIncident

@admin.register(BehaviorIncident)
class BehaviorIncidentAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "period", "place", "category")
    list_filter  = ("date", "category")
    search_fields = ("student__first_name_ar", "student__last_name_ar", "place", "category")
    date_hierarchy = "date"
