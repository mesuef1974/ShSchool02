import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.people.models import Student

class Route(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف المسار"))
    code = models.CharField(max_length=50, unique=True, verbose_name=_("رمز المسار"))
    capacity = models.IntegerField(default=0, verbose_name=_("السعة"))

    def __str__(self):
        return f"مسار {self.code} (سعة {self.capacity})"

    class Meta:
        verbose_name = _("مسار نقل")
        verbose_name_plural = _("مسارات النقل")

class RouteStop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف المحطة"))
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name=_("المسار"))
    seq = models.IntegerField(verbose_name=_("الترتيب"))
    name = models.CharField(max_length=200, verbose_name=_("اسم المحطة"))

    def __str__(self):
        return f"{self.route.code} – محطة {self.seq}: {self.name}"

    class Meta:
        unique_together = (("route","seq"),)
        verbose_name = _("محطة")
        verbose_name_plural = _("محطات")

class StudentRider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("معرّف الركاب"))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("الطالب"))
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name=_("المسار"))

    def __str__(self):
        return f"{self.student} ↔ {self.route.code}"

    class Meta:
        unique_together = (("student","route"),)
        verbose_name = _("مستقل حافلة")
        verbose_name_plural = _("مستقلو الحافلات")
