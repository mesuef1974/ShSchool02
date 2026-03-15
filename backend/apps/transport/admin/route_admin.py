from django.contrib import admin
from ..models import TransportRoute

@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'capacity', 'supervisor_staff_id', 'driver_name', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('code', 'driver_name')

