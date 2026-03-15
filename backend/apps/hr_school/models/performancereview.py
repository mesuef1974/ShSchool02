from django.db import models
from apps.people.models import Staff
from apps.core.models import Year

class PerformanceReview(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True, default="")
    # ...existing code...

