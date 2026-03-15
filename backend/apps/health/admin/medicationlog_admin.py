from django.contrib import admin
from ..models import MedicationLog

@admin.register(MedicationLog)
class MedicationLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'medicine', 'dose')
    search_fields = ('student__id', 'medicine')
    # يمكن إضافة مزيد من التخصيص لاحقاً
