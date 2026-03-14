
from rest_framework import serializers
from .models import Exam, ExamResult, Appeal

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = "__all__"

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = "__all__"
