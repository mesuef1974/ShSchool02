from rest_framework import viewsets
from .models import BehaviorIncident
from .serializers import BehaviorIncidentSerializer
from apps.identity.permissions import HasRBACPermission
class BehaviorIncidentViewSet(viewsets.ModelViewSet): queryset=BehaviorIncident.objects.all(); serializer_class=BehaviorIncidentSerializer; permission_resource="behavior"; permission_classes=[HasRBACPermission]
