from django.db import models

class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=120)
    record_id = models.CharField(max_length=64)
    actor_user = models.CharField(max_length=120)
    action = models.CharField(max_length=10)
    old_values = models.JSONField(null=True, blank=True)
    new_values = models.JSONField(null=True, blank=True)
    ip = models.CharField(max_length=50, blank=True, default="")
    ua = models.CharField(max_length=200, blank=True, default="")
    ts = models.DateTimeField(auto_now_add=True)

class OutboxEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=120)
    payload = models.JSONField()
    status = models.CharField(max_length=20, default='pending')
    ts = models.DateTimeField(auto_now_add=True)
