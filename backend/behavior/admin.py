from django.contrib import admin
from .models import OffenseCode, BehaviorIncident, BehaviorCommittee, BehaviorSanction

@admin.register(OffenseCode)
class OffenseCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'severity', 'description')
    list_filter = ('severity',)
    search_fields = ('code', 'description')  # Added search_fields

class BehaviorSanctionInline(admin.TabularInline):
    model = BehaviorSanction
    extra = 0

class BehaviorCommitteeInline(admin.StackedInline):
    model = BehaviorCommittee
    extra = 0

@admin.register(BehaviorIncident)
class BehaviorIncidentAdmin(admin.ModelAdmin):
    list_display = ('student', 'offense_code', 'date')
    list_filter = ('offense_code__severity', 'date')
    search_fields = ('student__national_id', 'student__first_name_ar')
    autocomplete_fields = ['student', 'offense_code']
    inlines = [BehaviorCommitteeInline, BehaviorSanctionInline]
    date_hierarchy = 'date'
