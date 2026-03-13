from django.contrib import admin
from .models import NoticeTemplate, Notice

@admin.register(NoticeTemplate)
class NoticeTemplateAdmin(admin.ModelAdmin):
    list_display = ('code', 'channel', 'subject')
    list_filter = ('channel',)
    search_fields = ('code', 'subject')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('student', 'notice_type', 'channel', 'sent_at')
    list_filter = ('notice_type', 'channel', 'sent_at')
    search_fields = ('student__national_id',)
    date_hierarchy = 'sent_at'
