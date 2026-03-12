from django.contrib import admin
from .models import OffenseCode, BehaviorIncident, BehaviorCommittee, BehaviorSanction

admin.site.register(OffenseCode)
admin.site.register(BehaviorIncident)
admin.site.register(BehaviorCommittee)
admin.site.register(BehaviorSanction)
