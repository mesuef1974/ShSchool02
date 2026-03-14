from rest_framework import viewsets
from .models import LibraryTitle,LibraryCopy,LibraryLoan
from .serializers import LibraryTitleSerializer,LibraryCopySerializer,LibraryLoanSerializer
from apps.identity.permissions import HasRBACPermission
class LibraryTitleViewSet(viewsets.ModelViewSet): queryset=LibraryTitle.objects.all(); serializer_class=LibraryTitleSerializer; permission_resource="library"; permission_classes=[HasRBACPermission]
class LibraryCopyViewSet(viewsets.ModelViewSet): queryset=LibraryCopy.objects.all(); serializer_class=LibraryCopySerializer; permission_resource="library"; permission_classes=[HasRBACPermission]
class LibraryLoanViewSet(viewsets.ModelViewSet): queryset=LibraryLoan.objects.all(); serializer_class=LibraryLoanSerializer; permission_resource="library"; permission_classes=[HasRBACPermission]
