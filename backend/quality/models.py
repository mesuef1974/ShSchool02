from django.db import models
from backend.common.models import BaseFormFields

class QualityStandard(BaseFormFields):
    code = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)

class QualityIndicator(BaseFormFields):
    standard = models.ForeignKey(QualityStandard, on_delete=models.CASCADE)
    indicator = models.CharField(max_length=128)

class QualityEvidence(BaseFormFields):
    indicator = models.ForeignKey(QualityIndicator, on_delete=models.CASCADE)
    evidence = models.CharField(max_length=256)
    file_ref = models.CharField(max_length=256, null=True, blank=True)
# سيتم بناء نموذج QualityStandard وQualityIndicator وQualityEvidence هنا حسب ملفات التوثيق.
