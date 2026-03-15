from django.contrib import admin
from ..models import TransportRideLog

@admin.register(TransportRideLog)
class TransportRideLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_id', 'date', 'departed_at', 'arrived_at', 'notes', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('route_id', 'date')

