from django.contrib import admin
from .models import TimetableRule, TimetableSlot

@admin.register(TimetableRule)
class TimetableRuleAdmin(admin.ModelAdmin):
    pass

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):
    pass

