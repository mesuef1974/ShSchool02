# backend/context_processors.py
from django.conf import settings

def admin_ui_settings(request):
    """
    يمرّر إعدادات واجهة الإدمن (ترتيب وألوان التطبيقات) إلى القوالب.
    إذا لم تكن القيم معرّفة في settings.py، يستخدم قيمًا افتراضية فارغة.
    """
    return {
        "ADMIN_APP_ORDER":  getattr(settings, "ADMIN_APP_ORDER", []),
        "ADMIN_APP_COLORS": getattr(settings, "ADMIN_APP_COLORS", {}),
    }