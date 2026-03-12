from django.db import models
from backend.common.models import BaseFormFields

class Notice(BaseFormFields):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField()
    channel = models.CharField(max_length=32)  # SMS/Email/Letter
# سيتم بناء نموذج Notice هنا حسب ملفات التوثيق.
