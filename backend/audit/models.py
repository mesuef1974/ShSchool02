from django.db import models
from backend.common.models import BaseFormFields

class AuditLog(BaseFormFields):
    user_id = models.UUIDField()
    action = models.CharField(max_length=64)
    target = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)
