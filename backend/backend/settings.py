# -*- coding: utf-8 -*-
# =========================
# Settings – Shahania School (Django)
# =========================
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# =========================
# المسارات وملف البيئة
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# =========================
# الإعدادات الأساسية
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

# استخدم true/false من .env (افتراضي True للتطوير المحلي)
DEBUG = os.getenv("DEBUG", "true").strip().lower() == "true"

# نحول قائمة المضيفين من env إلى list
# مثال في .env: ALLOWED_HOSTS=127.0.0.1,localhost,school.example.com
ALLOWED_HOSTS = [
    h.strip()
    for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if h.strip()
]

# اختياري: مصادر موثوقة لـ CSRF (ضروري عند استخدام دومين/بروكسي)
# مثال في .env: CSRF_TRUSTED_ORIGINS=https://school.example.com,https://*.example.net
_csrf_trusted = [
    o.strip()
    for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]
if _csrf_trusted:
    CSRF_TRUSTED_ORIGINS = _csrf_trusted

# =========================
# التطبيقات
# =========================
INSTALLED_APPS = [
    # =====================
    # Django default apps
    # =====================
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # =====================
    # 3rd‑party packages
    # =====================
    "rest_framework",          # DRF
    "django_filters",          # django-filters
    "drf_spectacular",         # OpenAPI schema
    # "django_extensions",     # سيُضاف اختياريًا بالأسفل لو متاح

    # =====================
    # Shahania School Apps (AppConfig Arabic)
    # =====================
    "apps.core.apps.CoreConfig",
    "apps.people.apps.PeopleConfig",
    "apps.timetable.apps.TimetableConfig",
    "apps.attendance.apps.AttendanceConfig",
    "apps.assessment.apps.AssessmentConfig",
    "apps.behavior.apps.BehaviorConfig",
    "apps.health.apps.HealthConfig",
    "apps.transport.apps.TransportConfig",
    "apps.library.apps.LibraryConfig",
    "apps.refdata.apps.RefdataConfig",
    "apps.identity.apps.IdentityConfig",

    # 🔽 تمت إضافتها لتظهر النماذج الجديدة في لوحة الإدارة
    "apps.assets.apps.AssetsConfig",
    "apps.comms.apps.CommsConfig",
    "apps.quality.apps.QualityConfig",
    "apps.audit.apps.AuditConfig",
    "apps.hr_school.apps.HrSchoolConfig",
]

# ➕ اجعل django_extensions اختياريًا (لا يوقف المشروع إن لم تُثبّت الحزمة)
try:
    import django_extensions  # noqa: F401
    INSTALLED_APPS.append("django_extensions")
except Exception:
    pass

# =========================
# الوسائط (Middleware)
# ملاحظة: WhiteNoise يجب أن يأتي بعد SecurityMiddleware مباشرة.
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ⭐ لخدمة static مع DEBUG=False
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",   # لدعم تعدد اللغات/الاتجاه RTL
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

# =========================
# القوالب
# =========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # مسار قوالب المشروع (ضع فيه templates/admin/index.html)
        "APP_DIRS": True,  # مهم لتحميل قوالب Django الافتراضية (admin/templates)
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # اختياري (مفيد للوصول إلى STATIC_URL و MEDIA_URL داخل القوالب)
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                # ⭐ يمرّر ADMIN_APP_ORDER و ADMIN_APP_COLORS للقوالب
                "backend.context_processors.admin_ui_settings",
            ],
            # "builtins": [], # إن أردت تحميل مكتبات template tags تلقائيًا (غير ضروري الآن)
        },
    }
]

WSGI_APPLICATION = "backend.wsgi.application"

# =========================
# قاعدة البيانات (PostgreSQL)
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PG_NAME", "shahania_db"),
        "USER": os.getenv("PG_USER", "sh_user"),
        "PASSWORD": os.getenv("PG_PASSWORD", "ChangeMe@123"),
        "HOST": os.getenv("PG_HOST", "127.0.0.1"),
        "PORT": os.getenv("PG_PORT", "5432"),
        "CONN_MAX_AGE": 60,  # إبقاء الاتصالات مفتوحة لدقيقة لتحسين الأداء
    }
}

# =========================
# اللغة والوقت
# =========================
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Qatar"
USE_I18N = True
USE_TZ = True

# مجلدات ملفات الترجمة (اختياري)
LOCALE_PATHS = [BASE_DIR / "locale"]

# =========================
# الملفات الثابتة والوسائط
# =========================
STATIC_URL = "/static/"
# في الإنتاج سنجمع هنا عبر collectstatic. هذا المجلد لديك ممتلئ بالفعل.
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# تخزين مضغوط + مانيفست لنسخ الإنتاج (ضروري مع WhiteNoise)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# مفاتيح/إعدادات مخصّصة
# =========================
APP_ENC_KEY = os.getenv("APP_ENC_KEY")  # مفتاح تشفير الحقول الحساسة (Fernet base64)

# =========================
# DRF + JWT + SPECTACULAR
# =========================
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    # مصادقة JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # افتراضيًا نجعل كل شيء يتطلب تسجيل دخول
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

# إعدادات SimpleJWT (يمكن تعديل مدد الصلاحية)
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,  # استخدام مفتاح المشروع للتوقيع
    "AUTH_HEADER_TYPES": ("Bearer",),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Shahania School API",
    "DESCRIPTION": "واجهات منصة مدرسة الشحانية",
    "VERSION": "0.2",
    "SERVE_INCLUDE_SCHEMA": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SCHEMA_PATH_PREFIX": r"/api",
}

# =========================
# Admin UI: ترتيب التطبيقات وألوانها
# =========================
ADMIN_APP_ORDER = [
    "identity", "people", "attendance", "timetable",
    "assessment", "behavior", "health", "transport",
    "library", "refdata", "auth", "core",
    # بإمكانك ترتيب الجديدة كذلك:
    "assets", "comms", "quality", "audit", "hr_school",
]

ADMIN_APP_COLORS = {
    "identity": "#8A1538",   # ماروني (Al Adaam)
    "people": "#59D3A0",     # أخضر فاتح
    "attendance": "#61B5F5", # أزرق فاتح
    "timetable": "#8A1538",
    "assessment": "#59D3A0",
    "behavior": "#61B5F5",
    "health": "#8A1538",
    "transport": "#59D3A0",
    "library": "#61B5F5",
    "refdata": "#8A1538",
    "auth": "#999999",
    "core": "#999999",
    "assets": "#59D3A0",
    "comms": "#61B5F5",
    "quality": "#8A1538",
    "audit": "#999999",
    "hr_school": "#59D3A0",
}

# =========================
# أمان (إعدادات إنتاج) – تُفعّل تلقائيًا عند DEBUG=False
# =========================
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
    # يُنصح بإضافة HSTS عند النشر خلف HTTPS فقط
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True