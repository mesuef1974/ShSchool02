from rest_framework import viewsets, filters
from .models import School,Year,Term,Subject,ClassRoom,Room
from .serializers import SchoolSerializer,YearSerializer,TermSerializer,SubjectSerializer,ClassRoomSerializer,RoomSerializer
from apps.identity.permissions import HasRBACPermission
class BaseVS(viewsets.ModelViewSet):
    permission_classes=[HasRBACPermission]
    filter_backends=[filters.SearchFilter]
class SchoolViewSet(BaseVS): queryset=School.objects.all(); serializer_class=SchoolSerializer; permission_resource='refdata'
class YearViewSet(BaseVS): queryset=Year.objects.all(); serializer_class=YearSerializer; permission_resource='refdata'
class TermViewSet(BaseVS): queryset=Term.objects.all(); serializer_class=TermSerializer; permission_resource='refdata'
class SubjectViewSet(BaseVS): queryset=Subject.objects.all(); serializer_class=SubjectSerializer; permission_resource='refdata'
class ClassRoomViewSet(BaseVS): queryset=ClassRoom.objects.all(); serializer_class=ClassRoomSerializer; permission_resource='core'
class RoomViewSet(BaseVS): queryset=Room.objects.all(); serializer_class=RoomSerializer; permission_resource='core'
