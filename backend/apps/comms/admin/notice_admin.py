from django.contrib import admin
from apps.comms.models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "audience", "published_on")
    search_fields = ("title", "audience")
    ordering = ("published_on",)

