Shahania – Patch التعريب الكامل + __str__ (v0.2)
Generated: 2026-03-14 19:13:58

هذا الباتش يضيف:
1) __str__ لكل النماذج لعرض أسماء عربية واضحة في Django Admin والقوائم المنسدلة.
2) verbose_name / verbose_name_plural عربي لكل Model.
3) AppConfig.verbose_name عربي لكل تطبيق لتظهر أسماء التطبيقات بالعربية في القائمة الجانبية.
4) تخصيص عناوين لوحة الإدارة (site_header/site_title/index_title) عبر ملف اختيارِي.

طريقة التركيب:
1) انسخ محتوى مجلد apps/<app> فوق مشروعك: D:/ShSchool02/backend/apps/<app>/
2) انسخ backend_admin_header.py إلى: D:/ShSchool02/backend/backend_admin_header.py (اختياري)
3) أضف في backend/urls.py قبل urlpatterns:
   from django.contrib import admin
   import backend_admin_header  # يضبط عناوين لوحة الإدارة
4) حدث INSTALLED_APPS لاستخدام AppConfig لكل تطبيق، مثلاً:
   'apps.core.apps.CoreConfig', 'apps.people.apps.PeopleConfig', ...
5) أعد تشغيل الخادم ثم افتح /admin
