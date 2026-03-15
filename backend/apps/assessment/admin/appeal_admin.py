from django.contrib import admin
from apps.assessment.models import Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ("exam", "reason", "decision", "enrollment_id", "created_at")
    search_fields = ("exam__name", "reason", "decision")
    ordering = ("exam", "enrollment_id")
