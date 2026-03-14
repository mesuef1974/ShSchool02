from django.db import models

class School(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True, default="")
    moehe_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Year(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    label = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

class Term(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        unique_together = (('year','code'),)

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True, default="")

class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    grade = models.SmallIntegerField()
    section = models.CharField(max_length=10)
    class Meta:
        unique_together = (('school','year','grade','section'),)

class Room(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(default=0)
