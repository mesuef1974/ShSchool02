from django.db import models

class Notice(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    audience = models.CharField(max_length=80, default='all')
    published_on = models.DateField()

