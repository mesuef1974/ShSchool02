from django.contrib import admin
from .models import LibraryTitle, LibraryCopy, LibraryLoan, Reservation

@admin.register(LibraryTitle)
class LibraryTitleAdmin(admin.ModelAdmin):
    list_display = ('title_ar', 'isbn', 'author_ar')
    search_fields = ('title_ar', 'isbn', 'author_ar')

class LibraryCopyInline(admin.TabularInline):
    model = LibraryCopy
    extra = 1

@admin.register(LibraryLoan)
class LibraryLoanAdmin(admin.ModelAdmin):
    list_display = ('copy', 'borrower_id', 'loan_date', 'due_date', 'return_date')
    list_filter = ('loan_date', 'due_date')
    search_fields = ('copy__copy_code', 'borrower_id')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title', 'requester_id', 'reserved_at', 'fulfilled')
    list_filter = ('reserved_at', 'fulfilled')
    search_fields = ('title__title_ar', 'requester_id')
