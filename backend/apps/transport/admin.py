from django.contrib import admin
from .models import TransportRoute, TransportRouteStop, TransportStudentRider, TransportRideLog, TransportDelayLog

@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    pass

@admin.register(TransportRouteStop)
class TransportRouteStopAdmin(admin.ModelAdmin):
    pass

@admin.register(TransportStudentRider)
class TransportStudentRiderAdmin(admin.ModelAdmin):
    pass

@admin.register(TransportRideLog)
class TransportRideLogAdmin(admin.ModelAdmin):
    pass

@admin.register(TransportDelayLog)
class TransportDelayLogAdmin(admin.ModelAdmin):
    pass

