# Shahania School – Backend & Database (v0.1)

**آخر تحديث**: 2026-03-14 17:28:45 (UTC+03)

هذا المستودع يوفّر **باك‑إند كامل (Django + DRF)** مع **قاعدة بيانات PostgreSQL** (CRUD + قيود فريدة + UUID + تشفير أعمدة حساسة على مستوى التطبيق) وفق الدليل التشغيلي الذي اتفقنا عليه لمدرسة الشحانية الإعدادية الثانوية.

> **توافق**: يعتمد هذا الإصدار على أفضل الممارسات ويأخذ بعين الاعتبار: قانون حماية البيانات الشخصية في قطر (PDPPL 13/2016)، الاعتماد الوطني QNSA، هيكل الوزارة (القرار الأميري 35/2022). راجع دليل السياسات في `docs/`.

---
## تشغيل محلي (بدون Docker)

1. أنشئ بيئة Python 3.11+ وافتحها ثم ثبّت المتطلبات:

```bash
python -m venv .venv
source .venv/bin/activate   # أو .venv\Scripts\activate على Windows
pip install --upgrade pip
pip install -r requirements.txt
```

2. أنشئ ملف البيئة `.env` من `.env.example` ثم حرّر كلمات السر والمفاتيح.

3. جهّز PostgreSQL:
```sql
CREATE USER sh_user WITH PASSWORD 'ChangeMe@123';
CREATE DATABASE shahania_db OWNER sh_user;
\c shahania_db
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

4. شغّل المهاجرات وحمّل البيانات المرجعية:
```bash
python manage.py migrate
python manage.py createsuperuser  # أنشئ حساب إدارة
python manage.py load_initial_data  # يحمّل القواميس الأساسية والأدوار
python manage.py runserver
```

> لوحة الإدارة: http://127.0.0.1:8000/admin

---
## ما الذي يشمله هذا الإصدار؟

- **تطبيقات**: identity, core, people, timetable, attendance, assessment, behavior, health, transport, library, hr_school, quality, assets, comms, audit, refdata
- **نماذج أساسية** مع قيود فريدة مطابقة للاتفاق (مثل: `uq_term_year_code`, `uq_class_room_school_year_grade_section`, `uq_attendance_record_enrollment_date_period`, `uq_exam_result_enrollment_exam`, `uq_appeal_enrollment_exam`).
- **تشفير**: أعمدة حساسة في العيادة/السلوك عبر طبقة تطبيق (Fernet/AES) مع تخزين بايتات مشفّرة (`bytea`).
- **RBAC** بذور أوّلية في `rbac/roles_permissions.json`.
- **SQL DDL** مكمّل في `db/sql/001_init.sql` (اختياري – يمكنك الاعتماد على مهاجرات Django).

---
## بنية المجلدات

```
Shahania_Backend_DB_v0_1/
  backend/ (مشروع Django)
  apps/    (تطبيقات المجالات)
  db/sql/  (DDL مكمّل)
  docs/    (سياسات وامتثال مختصر)
  rbac/    (بذور أدوار وصلاحيات)
  requirements.txt
  manage.py
  .env.example
  README.md
```

---
## ملاحظات امتثال مختصرة
- **PDPPL (13/2016)**: تشفير بيانات الطفل والصحة والسلوك وتقييد الوصول وتسجيله.
- **QNSA**: جداول `quality_evidence`, `improvement_plan`, `kpi_snapshot` للأدلّة ومتابعة التحسين.
- **الدفاع المدني**: ربط الغرف/الأصول بشهادات السلامة ومواعيد الصلاحية.

انظر `docs/policies_digest_ar.md` للتفاصيل.
