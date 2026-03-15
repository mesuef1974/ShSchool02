from django.db import models

class Nationality(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name_ar = models.CharField(max_length=120)
    name_en = models.CharField(max_length=120)
    class Meta:
        db_table = "refdata_lookup_nationality"
        managed = True

