
from django.contrib import admin
from .models import Exam, ExamResult, Appeal

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "term_code")
    list_filter  = ("subject", "term_code")
    search_fields = ("name",)

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "exam", "score")
    list_filter  = ("exam__subject",)
    search_fields = ("enrollment__student__first_name_ar", "enrollment__student__last_name_ar")

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "exam")
    list_filter  = ("exam__subject",)
