# backend/urls.py
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", RedirectView.as_view(url="/admin/", permanent=False)),  # توجيه الجذر
    path("admin/", admin.site.urls),
]

# خدمة الملفات الثابتة/الوسائط أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)