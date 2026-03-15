from django.db import models

class AbsenceReason(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name_ar = models.CharField(max_length=120)
    class Meta:
        db_table = "refdata_lookup_absence_reason"
        managed = True

