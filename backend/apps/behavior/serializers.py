from rest_framework import serializers
from .models import BehaviorIncident
class BehaviorIncidentSerializer(serializers.ModelSerializer):
    class Meta: model=BehaviorIncident; fields="__all__"
