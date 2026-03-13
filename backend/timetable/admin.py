from django.contrib import admin
from .models import Room, TimetableRule, TimetableSlot

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'type')
    list_filter = ('type',)
    search_fields = ('name',) # Added search_fields

@admin.register(TimetableRule)
class TimetableRuleAdmin(admin.ModelAdmin):
    list_display = ('school', 'year')
    list_filter = ('school', 'year')

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):
    list_display = ('class_room', 'day_of_week', 'period', 'subject', 'teacher')
    list_filter = ('day_of_week', 'class_room__grade', 'teacher')
    search_fields = ('subject__name_ar',)
    autocomplete_fields = ['class_room', 'subject', 'teacher', 'room']
