from django.db import models

class LookupNationality(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120, blank=True, default="")

class LookupAbsenceReason(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name_ar = models.CharField(max_length=120)
