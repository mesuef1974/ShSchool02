from django.db import models

class TimetableRule(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    row_version = models.IntegerField(default=1)
    class Meta:
        db_table = "timetable_timetablerule"
        managed = True

