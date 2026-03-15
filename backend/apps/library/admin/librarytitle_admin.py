from django.contrib import admin
from ..models import LibraryTitle

@admin.register(LibraryTitle)
class LibraryTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'author', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('isbn', 'title', 'author')

