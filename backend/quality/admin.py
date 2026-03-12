from django.contrib import admin
from .models import *

for model in [QualityStandard, QualityIndicator, QualityEvidence]:
    admin.site.register(model)
