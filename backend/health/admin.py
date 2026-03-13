from django.contrib import admin
from .models import ClinicVisit, MedicationLog

class MedicationLogInline(admin.TabularInline):
    model = MedicationLog
    extra = 1

@admin.register(ClinicVisit)
class ClinicVisitAdmin(admin.ModelAdmin):
    list_display = ('student', 'visited_at', 'retention_until')
    date_hierarchy = 'visited_at'
    search_fields = ('student__national_id',)
    autocomplete_fields = ['student']
    inlines = [MedicationLogInline]
    readonly_fields = ('complaint_enc', 'diagnosis_enc', 'action_taken_enc') # Encrypted fields shown as bytes
