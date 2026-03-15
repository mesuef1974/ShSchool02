from django.contrib import admin
from apps.comms.models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("body", "target", "sent_on")
    search_fields = ("body", "target")
    ordering = ("sent_on",)

