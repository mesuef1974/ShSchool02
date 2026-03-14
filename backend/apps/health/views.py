
from rest_framework import viewsets
from apps.identity.permissions import HasRBACPermission
from .models import ClinicVisit
from .serializers import ClinicVisitSerializer

class ClinicVisitViewSet(viewsets.ModelViewSet):
    queryset = ClinicVisit.objects.all()
    serializer_class = ClinicVisitSerializer
    permission_resource = "health"
    permission_classes = [HasRBACPermission]
