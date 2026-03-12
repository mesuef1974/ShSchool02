from django.contrib import admin
from .models import LibraryTitle, LibraryCopy, LibraryLoan

admin.site.register(LibraryTitle)
admin.site.register(LibraryCopy)
admin.site.register(LibraryLoan)
