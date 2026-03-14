from django.db import models

class QualityEvidence(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    domain = models.CharField(max_length=80)  # Leadership/Teaching/Learner Care/Resources/Self-Study
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    file_link = models.CharField(max_length=500, blank=True, default="")

class ImprovementPlan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    objective = models.CharField(max_length=300)
    owner = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.SmallIntegerField(default=0)

class KpiSnapshot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    taken_on = models.DateField()
