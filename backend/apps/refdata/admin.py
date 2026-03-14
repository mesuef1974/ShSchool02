
from django.contrib import admin
from .models import LookupNationality, LookupAbsenceReason

@admin.register(LookupNationality)
class LookupNationalityAdmin(admin.ModelAdmin):
    list_display = ("code", "name_ar", "name_en")
    search_fields = ("code", "name_ar", "name_en")

@admin.register(LookupAbsenceReason)
class LookupAbsenceReasonAdmin(admin.ModelAdmin):
    list_display = ("code", "name_ar")
    search_fields = ("code", "name_ar")
