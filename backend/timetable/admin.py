from django.contrib import admin
from .models import TimetableSlot, TimetableRule

admin.site.register(TimetableSlot)
admin.site.register(TimetableRule)
