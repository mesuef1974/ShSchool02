from django.contrib import admin
from .models import Bus, Route, RouteStop, StudentRider, RideLog, DelayLog

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('plate', 'capacity', 'gps_enabled', 'cctv_enabled')
    search_fields = ('plate',)

class RouteStopInline(admin.TabularInline):
    model = RouteStop
    extra = 1

@admin.register(RouteStop) # Registered as standalone admin for autocomplete support
class RouteStopAdmin(admin.ModelAdmin):
    list_display = ('route', 'seq', 'location')
    search_fields = ('location',)
    list_filter = ('route',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'bus')
    list_filter = ('bus',)
    search_fields = ('name',) # Added search_fields
    inlines = [RouteStopInline]

@admin.register(StudentRider)
class StudentRiderAdmin(admin.ModelAdmin):
    list_display = ('student', 'route', 'stop', 'active')
    list_filter = ('route', 'active')
    search_fields = ('student__national_id',)
    autocomplete_fields = ['student', 'route', 'stop']

@admin.register(RideLog)
class RideLogAdmin(admin.ModelAdmin):
    list_display = ('route', 'date', 'boarded', 'safety_check_pre', 'safety_check_post')
    list_filter = ('date', 'route')
    date_hierarchy = 'date'

@admin.register(DelayLog)
class DelayLogAdmin(admin.ModelAdmin):
    list_display = ('route', 'date', 'delay_minutes')
    list_filter = ('date', 'route')
    date_hierarchy = 'date'
