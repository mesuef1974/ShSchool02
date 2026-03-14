
from django.contrib import admin
from .models import School, Year, Term, Subject, ClassRoom, Room

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name_ar", "moehe_code")
    search_fields = ("name_ar", "name_en", "moehe_code")

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ("school", "label", "start_date", "end_date")
    list_filter  = ("school",)
    search_fields = ("label",)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("year", "code", "start_date", "end_date")
    list_filter  = ("year", "code")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name_ar", "name_en")
    search_fields = ("name_ar", "name_en")

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("school", "year", "grade", "section")
    list_filter  = ("school", "year", "grade")
    search_fields = ("section",)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("school", "code", "room_type", "capacity")
    list_filter  = ("school", "room_type")
    search_fields = ("code",)
