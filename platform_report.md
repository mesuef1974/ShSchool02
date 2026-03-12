# تقرير شامل للوضع الحالي لمنصة الشحانية (بدون مجلد DOCS)

## 1. نظرة عامة
- المنصة تعتمد على Django/PostgreSQL للباك اند، وTailwind/HTMX/Alpine للفرونت اند.
- الهيكلة modular: كل مجال في تطبيق مستقل (students, attendance, health, ...).
- واجهات Server-Rendered بملفات HTML منظمة، مع دعم RTL وهوية بصرية.

## 2. هيكلة المجلدات
### الجذر
- .env، .env.example
- .idea/ (إعدادات IDE)
- .venv/ (بيئة افتراضية)
- backend/ (كل الباك اند)
- docker-compose.yml، Dockerfile
- frontend/ (كل الفرونت اند)
- manage.py (تشغيل Django)
- now.zip (حزمة أرشيفية)
- platform_report.md (تقرير المنصة)
- README.md، requirements.txt

### Backend
- core/ (إعدادات المشروع)
- common/ (نماذج وأدوات مشتركة)
- accounts/ (المستخدمون وصلاحيات RBAC)
- students/ (نماذج الطالب، ولي الأمر، القيد)
- academics/ (المقررات والصفوف)
- attendance/ (الحضور والغياب)
- behavior، assessments، health، transport، library، quality، hr، timetable، notifications، audit (كل مجال في مجلد مستقل)
- templates/ (قوالب HTML)
- static/ (ملفات CSS/JS)

### Frontend
- src/css/app.css
- src/js/app.js
- tailwind.config.cjs
- package.json

## 3. إعدادات المشروع
- ملف .env لإدارة الأسرار وبيانات الاتصال.
- إعدادات Django منفصلة للبيئات (dev/prod/base).
- docker-compose.yml لتشغيل الخدمات (db, redis, web, worker).
- requirements.txt: جميع الحزم المطلوبة (Django، Celery، Redis، psycopg2، python-dotenv ...).

## 4. نماذج البيانات
- جميع الجداول تستخدم UUID كمفتاح أساسي.
- قيود تفرد وفهارس على الحقول الزمنية.
- نماذج رئيسية: Guardian, Student, School, AcademicYear, Term, Enrollment، Subject، ClassRoom، TeachingAssignment، AttendanceRecord.
- نماذج إضافية: Behavior، Assessments، Health، Transport، Library، Quality، HR، Timetable، Notifications، Audit.

## 5. القوالب والواجهات
- backend/templates/base.html (القالب الأساسي)
- layout/header.html، sidebar.html، footer.html
- admin/base_site.html
- صفحات جزئية لكل مجال (students، attendance، ...)
- دعم HTMX وAlpine.js لتفاعلية عالية بدون SPA.
- ملفات CSS تدعم RTL (admin-rtl.css)

## 6. إعدادات الأمان والامتثال
- تشفير الحقول الحساسة (الصحة/السلوك) في التطبيق.
- سجل تدقيق AuditLog.
- RBAC عبر مجموعات وصلاحيات Seed.
- سياسات احتفاظ للبيانات.

## 7. التشغيل والاختبار
- أوامر التشغيل السريعة:
  ```bash
  python -m venv .venv && .venv\Scripts\activate
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  cd frontend
  npm install
  npm run dev
  ```
- اختبارات عبر pytest وcoverage.
- دعم CI/CD عبر GitHub Actions.

## 8. نقاط القوة
- Modular structure، قابلية التوسع، توثيق شامل، دعم التفاعلية والهوية.
- إعدادات أمان وامتثال قوية.
- سهولة التكامل مع REST/OpenAPI مستقبلاً.

## 9. نقاط الضعف
- بعض النماذج في التطبيقات الفرعية تحتاج استكمال.
- يوصى بتوثيق إضافي للكود (docstrings).
- تفعيل اختبارات تلقائية لكل وحدة.

## 10. التوصيات
- استكمال نماذج بقية الوحدات.
- تفعيل اختبارات تلقائية وصيانة دورية.
- مراجعة الأمان بشكل دوري.
- توثيق الخدمات والعمليات business logic.
- مراجعة الأداء عند التوسع.

---

هذا التقرير يعكس الوضع الحالي للمنصة بالكامل (بدون مجلد DOCS)، ويصلح للاستخدام الإداري والفني.

