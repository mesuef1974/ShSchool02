from django.db import models

class MessageTemplate(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=100, unique=True)
    channel = models.CharField(max_length=20)  # sms/email/push
    content = models.TextField()

