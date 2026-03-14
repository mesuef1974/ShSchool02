
from rest_framework import serializers
from .models import Route, StudentRider

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class StudentRiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRider
        fields = "__all__"
