from django.contrib import admin
from ..models import QualityCommittee

@admin.register(QualityCommittee)
class QualityCommitteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee_type', 'member_name', 'job_title', 'role_in_committee', 'responsibility', 'domain', 'created_at', 'updated_at', 'deleted_at', 'row_version')
    search_fields = ('member_name', 'job_title', 'role_in_committee', 'domain')

