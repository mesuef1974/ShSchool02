from django.contrib import admin
from .models import Nationality, Religion, AbsenceReason, BehaviorCategory

@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    pass

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    pass

@admin.register(AbsenceReason)
class AbsenceReasonAdmin(admin.ModelAdmin):
    pass

@admin.register(BehaviorCategory)
class BehaviorCategoryAdmin(admin.ModelAdmin):
    pass

