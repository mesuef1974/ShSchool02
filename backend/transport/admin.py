from django.contrib import admin
from .models import Bus, Route, RouteStop, StudentRider, RideLog

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(RouteStop)
admin.site.register(StudentRider)
admin.site.register(RideLog)
