
from rest_framework import viewsets
from apps.identity.permissions import HasRBACPermission
from .models import LibraryTitle, LibraryCopy, LibraryLoan
from .serializers import LibraryTitleSerializer, LibraryCopySerializer, LibraryLoanSerializer

class LibraryTitleViewSet(viewsets.ModelViewSet):
    queryset = LibraryTitle.objects.all()
    serializer_class = LibraryTitleSerializer
    permission_resource = "library"
    permission_classes = [HasRBACPermission]

class LibraryCopyViewSet(viewsets.ModelViewSet):
    queryset = LibraryCopy.objects.all()
    serializer_class = LibraryCopySerializer
    permission_resource = "library"
    permission_classes = [HasRBACPermission]

class LibraryLoanViewSet(viewsets.ModelViewSet):
    queryset = LibraryLoan.objects.all()
    serializer_class = LibraryLoanSerializer
    permission_resource = "library"
    permission_classes = [HasRBACPermission]
