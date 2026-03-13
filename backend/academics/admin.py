from django.contrib import admin
from .models import (
    School, AcademicYear, Term, Subject, ClassRoom, Teacher, TeachingAssignment
)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'moe_code', 'level')
    search_fields = ('name_ar', 'moe_code')

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at')
    ordering = ('-code',)
    exclude = ('academic_year',)
    search_fields = ('code',)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('code', 'year', 'created_at')
    list_filter = ('year',)
    search_fields = ('code',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_ar')
    search_fields = ('code', 'name_ar')

class TeachingAssignmentInline(admin.TabularInline):
    model = TeachingAssignment
    extra = 1
    autocomplete_fields = ['class_room', 'subject']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'staff_code')
    search_fields = ('user__username', 'staff_code')
    inlines = [TeachingAssignmentInline]
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('school', 'year', 'term', 'grade', 'section', 'capacity')
    list_filter = ('school', 'year', 'term', 'grade')
    search_fields = ('grade', 'section')
    autocomplete_fields = ['school', 'year', 'term']

@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'class_room', 'subject', 'weekly_load')
    list_filter = ('subject', 'class_room__grade')
    autocomplete_fields = ['teacher', 'class_room', 'subject']
