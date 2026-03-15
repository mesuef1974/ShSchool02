from django.contrib import admin
from .models import Asset, MaintenanceTicket, SafetyCertificate

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'room')

@admin.register(MaintenanceTicket)
class MaintenanceTicketAdmin(admin.ModelAdmin):
    list_display = ('asset', 'title', 'status')

@admin.register(SafetyCertificate)
class SafetyCertificateAdmin(admin.ModelAdmin):
    list_display = ('room', 'cert_type', 'valid_until', 'file_link')

