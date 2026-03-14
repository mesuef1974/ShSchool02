
from django.contrib import admin
from .models import TimetableRule, TimetableSlot

@admin.register(TimetableRule)
class TimetableRuleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):
    list_display = ("class_room", "day_of_week", "period", "subject", "teacher", "room")
    list_filter  = ("class_room__year", "day_of_week", "period", "subject")
