from django.contrib import admin
from apps.assets.models import MaintenanceTicket

@admin.register(MaintenanceTicket)
class MaintenanceTicketAdmin(admin.ModelAdmin):
    list_display = ("asset", "type", "priority", "opened_on", "closed_on")
    search_fields = ("asset__category", "type", "priority")
    ordering = ("opened_on", "priority")

