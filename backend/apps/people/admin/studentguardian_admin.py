from django.contrib import admin
from apps.people.models.studentguardian import StudentGuardian


@admin.register(StudentGuardian)
class StudentGuardianAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "guardian_id",
        "relation",
        "is_primary",
    )

    search_fields = (
        "student_id",
        "guardian_id",
        "relation",
    )

    list_filter = ("relation", "is_primary")

    ordering = ("student_id", "guardian_id")