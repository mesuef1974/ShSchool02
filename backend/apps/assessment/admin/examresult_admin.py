from django.contrib import admin
from apps.assessment.models import ExamResult

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("exam", "score", "enrollment_id", "created_at")
    search_fields = ("exam__name", "enrollment_id")
    ordering = ("exam", "enrollment_id")
