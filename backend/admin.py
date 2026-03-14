from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite

class ShahaniaAdminSite(AdminSite):
    site_header = "منصة مدرسة الشحانية – لوحة التحكم"
    site_title  = "إدارة مدرسة الشحانية"
    index_title = "مرحبًا بك"

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = list(app_dict.values())
        order = getattr(settings, "ADMIN_APP_ORDER", [])

        def app_pos(label):
            try:
                return order.index(label)
            except ValueError:
                return 999  # ما لم يُذكر، يذهب للنهاية

        app_list.sort(key=lambda a: app_pos(a["app_label"]))
        for app in app_list:
            app["models"].sort(key=lambda m: m["name"])  # ترتيب موديلات التطبيق
        return app_list

# استبدال الموقع الافتراضي بالمخصص
admin.site = ShahaniaAdminSite()
admin.autodiscover()