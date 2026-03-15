from django.contrib import admin
from ..models import AbsenceReason

@admin.register(AbsenceReason)
class AbsenceReasonAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ar')
    search_fields = ('code', 'name_ar')

