from django.contrib import admin
from .models import Notice, Announcement, MessageTemplate, DeliveryLog

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass

@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(DeliveryLog)
class DeliveryLogAdmin(admin.ModelAdmin):
    pass

