from django.contrib import admin
from apps.assessment.models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "term_code", "subject_id", "created_at")
    search_fields = ("name", "term_code")
    ordering = ("name",)
