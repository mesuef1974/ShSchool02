
from rest_framework import viewsets, filters
from apps.identity.permissions import HasRBACPermission
from .models import TimetableSlot
from .serializers import TimetableSlotSerializer

class TimetableSlotViewSet(viewsets.ModelViewSet):
    queryset = TimetableSlot.objects.all()
    serializer_class = TimetableSlotSerializer
    permission_resource = "timetable"
    permission_classes = [HasRBACPermission]
    filter_backends = [filters.SearchFilter]
