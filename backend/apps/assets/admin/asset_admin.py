from django.contrib import admin
from apps.assets.models import Asset

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("category", "model", "serial_no", "school", "room", "created_at")
    search_fields = ("category", "model", "serial_no")
    ordering = ("category", "model")

