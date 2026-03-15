from django.db import models
from .messagetemplate import MessageTemplate

class DeliveryLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True)
    recipient = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    sent_at = models.DateTimeField()

