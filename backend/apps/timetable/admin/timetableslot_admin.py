from django.contrib import admin
from ..models import TimetableSlot

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_of_week', 'period', 'class_room_id', 'room_id', 'subject_id', 'teacher_id', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('class_room_id', 'subject_id', 'teacher_id')

