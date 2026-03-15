from django.contrib import admin
from .models import LibraryTitle, LibraryCopy, LibraryLoan, Reservation

@admin.register(LibraryTitle)
class LibraryTitleAdmin(admin.ModelAdmin):
    pass

@admin.register(LibraryCopy)
class LibraryCopyAdmin(admin.ModelAdmin):
    pass

@admin.register(LibraryLoan)
class LibraryLoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

