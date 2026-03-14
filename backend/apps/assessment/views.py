from rest_framework import viewsets
from .models import Exam,ExamResult,Appeal
from .serializers import ExamSerializer,ExamResultSerializer,AppealSerializer
from apps.identity.permissions import HasRBACPermission
class ExamViewSet(viewsets.ModelViewSet): queryset=Exam.objects.all(); serializer_class=ExamSerializer; permission_resource="assessment"; permission_classes=[HasRBACPermission]
class ExamResultViewSet(viewsets.ModelViewSet): queryset=ExamResult.objects.all(); serializer_class=ExamResultSerializer; permission_resource="assessment"; permission_classes=[HasRBACPermission]
class AppealViewSet(viewsets.ModelViewSet): queryset=Appeal.objects.all(); serializer_class=AppealSerializer; permission_resource="assessment"; permission_classes=[HasRBACPermission]
