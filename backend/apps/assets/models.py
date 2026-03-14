from django.db import models
from apps.core.models import Room

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    serial = models.CharField(max_length=100, blank=True, default="")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

class MaintenanceTicket(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')

class SafetyCertificate(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    cert_type = models.CharField(max_length=120)
    valid_until = models.DateField()
    file_link = models.CharField(max_length=500, blank=True, default="")
