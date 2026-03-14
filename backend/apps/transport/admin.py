
from django.contrib import admin
from .models import Route, StudentRider

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("code", "capacity")
    search_fields = ("code",)

@admin.register(StudentRider)
class StudentRiderAdmin(admin.ModelAdmin):
    list_display = ("student", "route")
    list_filter  = ("route",)
    search_fields = ("student__first_name_ar", "student__last_name_ar")
