from django.contrib import admin
from .models import School, Year, Term, Grade, Subject, Room, ClassRoom

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'moehe_code')

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('school', 'label', 'start_date', 'end_date')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('year', 'code', 'start_date', 'end_date')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('code', 'label_ar', 'label_en')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('school', 'code', 'room_type', 'capacity')

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('school', 'year', 'grade', 'section')

