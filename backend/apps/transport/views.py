
from rest_framework import viewsets
from apps.identity.permissions import HasRBACPermission
from .models import Route, StudentRider
from .serializers import RouteSerializer, StudentRiderSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_resource = "transport"
    permission_classes = [HasRBACPermission]

class StudentRiderViewSet(viewsets.ModelViewSet):
    queryset = StudentRider.objects.all()
    serializer_class = StudentRiderSerializer
    permission_resource = "transport"
    permission_classes = [HasRBACPermission]
