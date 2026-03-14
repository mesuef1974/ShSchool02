from django.db import models

class Notice(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    audience = models.CharField(max_length=80, default='all')
    published_on = models.DateField()

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    body = models.TextField()
    target = models.CharField(max_length=120)
    sent_on = models.DateTimeField()

class MessageTemplate(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    code = models.CharField(max_length=100, unique=True)
    channel = models.CharField(max_length=20)  # sms/email/push
    content = models.TextField()

class DeliveryLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True)
    recipient = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    sent_at = models.DateTimeField()
