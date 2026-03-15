from django.conf import settings

def admin_ui_settings(request):
    """
    يمرّر إعدادات ترتيب وألوان التطبيقات إلى القالب.
    """
    return {
        "ADMIN_APP_ORDER": getattr(settings, "ADMIN_APP_ORDER", []),
        "ADMIN_APP_COLORS": getattr(settings, "ADMIN_APP_COLORS", {}),
    }