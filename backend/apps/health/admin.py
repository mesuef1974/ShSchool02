from django.contrib import admin
from .models import ClinicVisit, MedicationLog

@admin.register(ClinicVisit)
class ClinicVisitAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'reason')

@admin.register(MedicationLog)
class MedicationLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'medicine', 'dose')

