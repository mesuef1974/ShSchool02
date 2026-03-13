from django.contrib import admin
from django.urls import path

# Admin Site Configuration
admin.site.site_header = "إدارة مدرسة الشحانية الذكية"
admin.site.site_title = "نظام الشحانية"
admin.site.index_title = "لوحة التحكم الرئيسية"

urlpatterns = [
    path('admin/', admin.site.urls),
]
