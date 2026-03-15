from django.contrib import admin
from apps.comms.models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "start_on", "end_on", "school")
    search_fields = ("title", "content")
    ordering = ("start_on",)
