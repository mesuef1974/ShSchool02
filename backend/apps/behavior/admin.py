from django.contrib import admin
from .models import BehaviorIncident, BehaviorCommittee, BehaviorSanction

@admin.register(BehaviorIncident)
class BehaviorIncidentAdmin(admin.ModelAdmin):
    pass

@admin.register(BehaviorCommittee)
class BehaviorCommitteeAdmin(admin.ModelAdmin):
    pass

@admin.register(BehaviorSanction)
class BehaviorSanctionAdmin(admin.ModelAdmin):
    pass

