from django.db import models
from backend.common.models import ShahaniaBaseModel
from backend.students.models import Student

class Bus(ShahaniaBaseModel):
    plate = models.CharField(max_length=16, unique=True, verbose_name="رقم اللوحة")
    capacity = models.SmallIntegerField(null=True, blank=True, verbose_name="السعة")
    gps_enabled = models.BooleanField(default=True, verbose_name="GPS مفعّل")
    cctv_enabled = models.BooleanField(default=True, verbose_name="كاميرا مفعّلة")

class Route(ShahaniaBaseModel):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, verbose_name="الحافلة")
    name = models.CharField(max_length=64, verbose_name="اسم المسار")

class RouteStop(ShahaniaBaseModel):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="المسار")
    seq = models.SmallIntegerField(verbose_name="ترتيب الوقفة")
    location = models.CharField(max_length=256, null=True, blank=True, verbose_name="الموقع")

class StudentRider(ShahaniaBaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="المسار")
    stop = models.ForeignKey(RouteStop, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="نقطة الوقوف")
    active = models.BooleanField(default=True, verbose_name="نشط")

class RideLog(ShahaniaBaseModel):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="المسار")
    date = models.DateField(auto_now_add=True, verbose_name="التاريخ")
    boarded = models.SmallIntegerField(default=0, verbose_name="عدد الطلاب")
    safety_check_pre = models.BooleanField(default=False, verbose_name="فحص السلامة (قبل)")
    safety_check_post = models.BooleanField(default=False, verbose_name="فحص السلامة (بعد)")

class DelayLog(ShahaniaBaseModel):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="المسار")
    date = models.DateField(auto_now_add=True, verbose_name="التاريخ")
    arrival_time = models.TimeField(null=True, blank=True, verbose_name="وقت الوصول")
    delay_minutes = models.SmallIntegerField(default=0, verbose_name="دقائق التأخير")
