from django.contrib import admin
from apps.people.models.teachingassignment import TeachingAssignment


@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "teacher_id",
        "class_room_id",
        "subject_id",
    )

    search_fields = (
        "teacher_id",
        "class_room_id",
        "subject_id",
    )

    list_filter = ()

    ordering = ("teacher_id", "class_room_id", "subject_id")