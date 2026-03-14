
from rest_framework import viewsets, filters
from apps.identity.permissions import HasRBACPermission
from .models import AttendanceRecord
from .serializers import AttendanceRecordSerializer

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_resource = "attendance"
    permission_classes = [HasRBACPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["note"]
