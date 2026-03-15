from django.contrib import admin
from ..models import TransportRouteStop

@admin.register(TransportRouteStop)
class TransportRouteStopAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_id', 'seq', 'name', 'lat', 'lon', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('name', 'route_id')

