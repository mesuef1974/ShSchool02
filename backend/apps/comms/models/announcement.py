from django.db import models

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    body = models.TextField()
    target = models.CharField(max_length=120)
    sent_on = models.DateTimeField()

