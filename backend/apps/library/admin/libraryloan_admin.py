from django.contrib import admin
from ..models import LibraryLoan

@admin.register(LibraryLoan)
class LibraryLoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'copy', 'borrower_staff', 'borrower_student', 'issued_on', 'due_on', 'returned_on', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('copy__barcode', 'borrower_staff__id', 'borrower_student__id')

