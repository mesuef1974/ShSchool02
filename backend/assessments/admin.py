from django.contrib import admin
from .models import Exam, ExamSession, ExamResult

class ExamSessionInline(admin.TabularInline):
    model = ExamSession
    extra = 1

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'grade', 'term', 'is_makeup')
    list_filter = ('term', 'grade', 'is_makeup')
    search_fields = ('subject__name_ar',)
    inlines = [ExamSessionInline]

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'exam', 'score')
    list_filter = ('exam__term', 'score')
    search_fields = ('enrollment__student__national_id',)
    autocomplete_fields = ['enrollment', 'exam']
