from django.contrib import admin
from ..models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'copy', 'student', 'staff', 'reserved_on', 'expires_on', 'fulfilled', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('copy__barcode', 'student__id', 'staff__id')

