from django.contrib import admin
from apps.assets.models import SafetyCertificate

@admin.register(SafetyCertificate)
class SafetyCertificateAdmin(admin.ModelAdmin):
    list_display = ("certificate_type", "school", "room", "valid_until")
    search_fields = ("certificate_type", "school__name_ar", "room__code")
    ordering = ("certificate_type", "valid_until")

