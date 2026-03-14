
from rest_framework import viewsets, filters
from apps.identity.permissions import HasRBACPermission
from .models import Student, Guardian, Staff, Enrollment
from .serializers import (
    StudentSerializer, GuardianSerializer, StaffSerializer, EnrollmentSerializer
)

class BaseVS(viewsets.ModelViewSet):
    permission_classes = [HasRBACPermission]
    filter_backends = [filters.SearchFilter]

class StudentViewSet(BaseVS):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_resource = 'people'
    search_fields = ["first_name_ar", "last_name_ar", "email", "phone"]

class GuardianViewSet(BaseVS):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    permission_resource = 'people'

class StaffViewSet(BaseVS):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_resource = 'people'

class EnrollmentViewSet(BaseVS):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_resource = 'people'
