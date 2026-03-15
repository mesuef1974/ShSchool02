from django.contrib import admin
from ..models import ClinicVisit

@admin.register(ClinicVisit)
class ClinicVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'reason')
    search_fields = ('student__id', 'reason')
    # يمكن إضافة مزيد من التخصيص لاحقاً

