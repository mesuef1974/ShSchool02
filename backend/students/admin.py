from django.contrib import admin
from .models import Guardian, Student, Enrollment

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('full_name_ar', 'phone', 'relation')
    search_fields = ('full_name_ar', 'phone')

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    autocomplete_fields = ['student']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name_ar', 'last_name_ar', 'dob', 'guardian')
    search_fields = ('national_id', 'first_name_ar', 'last_name_ar')
    autocomplete_fields = ['guardian']
    inlines = [EnrollmentInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'school_id', 'year_id', 'grade', 'section')
    list_filter = ('school_id', 'year_id', 'grade')
    search_fields = ('student__national_id', 'student__first_name_ar')
    autocomplete_fields = ['student']
