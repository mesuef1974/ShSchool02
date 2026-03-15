from django.contrib import admin
from apps.comms.models import DeliveryLog

@admin.register(DeliveryLog)
class DeliveryLogAdmin(admin.ModelAdmin):
    list_display = ("template", "recipient", "status", "sent_at")
    search_fields = ("recipient", "status")
    ordering = ("sent_at",)

