from django.contrib import admin
from apps.assessment.models import ExamSession

@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ("exam", "room_id", "date", "start_time", "end_time")
    search_fields = ("exam__name", "room_id")
    ordering = ("date", "start_time")
