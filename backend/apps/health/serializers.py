
from rest_framework import serializers
from .models import ClinicVisit

class ClinicVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicVisit
        fields = "__all__"
