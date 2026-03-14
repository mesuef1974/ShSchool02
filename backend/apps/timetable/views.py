from rest_framework import viewsets
from .models import TimetableSlot
from .serializers import TimetableSlotSerializer
from apps.identity.permissions import HasRBACPermission
class TimetableSlotViewSet(viewsets.ModelViewSet):
    queryset=TimetableSlot.objects.all(); serializer_class=TimetableSlotSerializer; permission_resource="timetable"; permission_classes=[HasRBACPermission]
