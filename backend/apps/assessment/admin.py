from django.contrib import admin
from .models import Exam, ExamSession, ExamResult, Appeal

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'term_code', 'subject_id', 'created_at')

@admin.register(ExamSession)
class ExamSessionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'room_id', 'date', 'start_time', 'end_time', 'invigilator_staff_id')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'score', 'enrollment_id', 'created_at')

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('exam', 'reason', 'decision', 'enrollment_id', 'created_at')

