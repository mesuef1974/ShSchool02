from django.contrib import admin
from ..models import TransportDelayLog

@admin.register(TransportDelayLog)
class TransportDelayLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'ride_id', 'minutes_late', 'reason', 'notified', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('ride_id', 'reason')

