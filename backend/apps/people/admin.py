from django.contrib import admin
from .models import Student, Guardian, StudentGuardian, Staff, TeachingAssignment, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name_ar', 'last_name_ar', 'national_id', 'birth_date', 'gender', 'phone', 'email')

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name_ar', 'last_name_ar', 'phone', 'email')

@admin.register(StudentGuardian)
class StudentGuardianAdmin(admin.ModelAdmin):
    list_display = ('student', 'guardian', 'relation', 'is_primary')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name_ar', 'last_name_ar', 'job_title', 'email')

@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'class_room', 'subject')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'school', 'year', 'grade', 'class_room', 'status')

