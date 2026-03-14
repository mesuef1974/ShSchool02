from django.conf import settings

def admin_ui_settings(request):
    """
    Passes ADMIN_APP_ORDER and ADMIN_APP_COLORS to template context.
    """
    return {
        "ADMIN_APP_ORDER": getattr(settings, 'ADMIN_APP_ORDER', []),
        "ADMIN_APP_COLORS": getattr(settings, 'ADMIN_APP_COLORS', {}),
    }
