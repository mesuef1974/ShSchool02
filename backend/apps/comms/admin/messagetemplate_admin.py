from django.contrib import admin
from apps.comms.models import MessageTemplate

@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ("code", "channel")
    search_fields = ("code", "channel")
    ordering = ("code",)

