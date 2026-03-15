from django.contrib import admin
from ..models import PerformanceReview

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'year', 'score', 'comments')
    search_fields = ('staff__id', 'year__id')
    # ...existing code...

