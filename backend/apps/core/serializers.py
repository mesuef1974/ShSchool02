
from rest_framework import serializers
from .models import School, Year, Term, Subject, ClassRoom, Room

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
