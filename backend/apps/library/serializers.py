
from rest_framework import serializers
from .models import LibraryTitle, LibraryCopy, LibraryLoan

class LibraryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryTitle
        fields = "__all__"

class LibraryCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCopy
        fields = "__all__"

class LibraryLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryLoan
        fields = "__all__"
