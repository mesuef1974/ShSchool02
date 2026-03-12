from django.db import models
from backend.common.models import BaseFormFields

class TimetableSlot(BaseFormFields):
    class_room = models.ForeignKey('academics.ClassRoom', on_delete=models.CASCADE)
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('academics.Teacher', on_delete=models.CASCADE)
    slot_time = models.DateTimeField()
    room = models.CharField(max_length=64)

class TimetableRule(BaseFormFields):
    rule_json = models.JSONField()
