from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.academics.models import School, AcademicYear, ClassRoom, Subject, Teacher

class Room(ShahaniaBaseModel):
    name = models.CharField(max_length=64, verbose_name="اسم الغرفة")
    capacity = models.SmallIntegerField(null=True, blank=True, verbose_name="السعة")
    type = models.CharField(max_length=32, null=True, blank=True, verbose_name="النوع")

class TimetableRule(ShahaniaBaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="المدرسة")
    year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name="السنة")
    json_rule = models.JSONField(verbose_name="القاعدة")

class TimetableSlot(ShahaniaBaseModel):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="الفصل")
    day_of_week = models.SmallIntegerField(verbose_name="اليوم") # 1=Sun, 7=Sat
    period = models.SmallIntegerField(verbose_name="الحصة")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="المادة")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="المعلم")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الغرفة")
    is_fixed = models.BooleanField(default=False, verbose_name="ثابت")

    class Meta:
        unique_together = ('class_room', 'day_of_week', 'period')
