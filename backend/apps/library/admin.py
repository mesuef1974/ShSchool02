
from django.contrib import admin
from .models import LibraryTitle, LibraryCopy, LibraryLoan

@admin.register(LibraryTitle)
class LibraryTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn")
    search_fields = ("title", "author", "isbn")

@admin.register(LibraryCopy)
class LibraryCopyAdmin(admin.ModelAdmin):
    list_display = ("title", "barcode", "status")
    list_filter  = ("status",)
    search_fields = ("barcode", "title__title")

@admin.register(LibraryLoan)
class LibraryLoanAdmin(admin.ModelAdmin):
    list_display = ("copy", "issued_on", "due_on", "returned_on")
    list_filter  = ("issued_on", "due_on", "returned_on")
    date_hierarchy = "issued_on"
