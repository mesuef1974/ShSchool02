from django.contrib import admin
from ..models import LibraryCopy

@admin.register(LibraryCopy)
class LibraryCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'barcode', 'status', 'title', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('barcode', 'status')

