from django.db import models

class QualityCommittee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    committee_type = models.CharField(max_length=30, default='Quality')
    member_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=150)
    role_in_committee = models.CharField(max_length=50)
    responsibility = models.TextField(null=True, blank=True)
    domain = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)

