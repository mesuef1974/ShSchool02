
from django.contrib import admin
from .models import ClinicVisit

@admin.register(ClinicVisit)
class ClinicVisitAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "reason")
    list_filter  = ("date",)
    search_fields = ("student__first_name_ar", "student__last_name_ar", "reason")
    date_hierarchy = "date"
    readonly_fields = ("details_enc",)  # إخفاء المحتوى المُشفّر من التحرير المباشر
