# دليل إعداد منصة الشحانية – قسم الـ Backend (أوتوماتيكي)

هذا السكربت **`bootstrap_shahania_backend.ps1`** ينشئ مشروع Django، يضبط الإعدادات العربية وPostgreSQL من `.env`, يُنشئ جداول المصادقة (`auth_user`), ويعكس قاعدة البيانات إلى نماذج Django عبر `inspectdb` ثم يجهّز لوحة الإدارة لتسجيل كل النماذج.

## المتطلبات
- Python 3.10+
- PostgreSQL + أداة `psql` (اختياري لتشغيل ملف الـ DDL تلقائيًا)
- قاعدة بيانات ومستخدم كما في `.env`

## الاستخدام السريع
```powershell
# من مجلد المشروع الذي يحتوي ملف shahania_full_ddl_v1.sql
powershell -ExecutionPolicy Bypass -File .\bootstrap_shahania_backend.ps1

# ثم أنشئ مستخدم إدارة وشغّل السيرفر
.\.venv\Scripts\python manage.py createsuperuser
.\.venv\Scripts\python manage.py runserver
```

## ما الذي يفعله السكربت؟
1. إنشاء بيئة افتراضية وتثبيت (django, psycopg2-binary, python-dotenv)
2. إنشاء مشروع `backend` وتطبيق `school` إن لم يكونا موجودين
3. كتابة `.env` (إن لم يوجد) بالإعدادات الافتراضية التي زوّدتنا بها
4. تعديل `backend/settings.py` لقراءة `.env` وضبط اللغة العربية وPostgreSQL
5. تشغيل `migrate` لإنشاء جداول Django القياسية (ومنها `auth_user`)
6. (اختياري) تشغيل ملف DDL: `shahania_full_ddl_v1.sql` عبر `psql` إذا كان متوفرًا
7. تشغيل `inspectdb` وتوليد النماذج في `school/models.py`
8. تفعيل لوحة الإدارة بتسجيل تلقائي لكل النماذج

> **ملاحظة:** النماذج المولّدة ستكون غالبًا بـ `managed = False` حتى لا يحاول Django إدارتها بهجرات. يمكن تغيير ذلك لاحقًا لجداول محددة.
