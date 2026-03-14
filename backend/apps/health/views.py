from rest_framework import viewsets
from .models import ClinicVisit
from .serializers import ClinicVisitSerializer
from apps.identity.permissions import HasRBACPermission
class ClinicVisitViewSet(viewsets.ModelViewSet): queryset=ClinicVisit.objects.all(); serializer_class=ClinicVisitSerializer; permission_resource="health"; permission_classes=[HasRBACPermission]
