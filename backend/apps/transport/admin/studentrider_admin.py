from django.contrib import admin
from ..models import TransportStudentRider

@admin.register(TransportStudentRider)
class TransportStudentRiderAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_id', 'student_id', 'pickup_stop_id', 'dropoff_stop_id', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('student_id', 'route_id')

