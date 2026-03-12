from django.contrib import admin
from .models import Exam, ExamSession, ExamResult

admin.site.register(Exam)
admin.site.register(ExamSession)
admin.site.register(ExamResult)
