
from django.contrib import admin
from .models import Student, Guardian, StudentGuardian, Staff, TeachingAssignment, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name_ar", "last_name_ar", "gender", "birth_date")
    search_fields = ("first_name_ar", "last_name_ar", "first_name_en", "last_name_en", "email", "phone")
    list_filter = ("gender",)

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ("first_name_ar", "last_name_ar", "phone", "email")
    search_fields = ("first_name_ar", "last_name_ar", "phone", "email")

@admin.register(StudentGuardian)
class StudentGuardianAdmin(admin.ModelAdmin):
    list_display = ("student", "guardian", "relation", "is_primary")
    list_filter = ("relation", "is_primary")

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("first_name_ar", "last_name_ar", "job_title", "email")
    search_fields = ("first_name_ar", "last_name_ar", "job_title", "email")

@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "class_room", "subject")
    list_filter = ("class_room__year", "class_room__grade", "subject")

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "school", "year", "grade", "class_room", "status")
    list_filter  = ("school", "year", "grade", "status")
    search_fields = ("student__first_name_ar", "student__last_name_ar")
