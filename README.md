
# منصة الشحانية — Full‑Stack RTL (Django + PostgreSQL + Tailwind + HTMX + Alpine)

## تشغيل سريع
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=core.settings.dev
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## إعداد واجهة Tailwind
```bash
cd frontend
npm install
npm run dev   # مراقبة مستمرة — يكتب إلى backend/static/css/app.css و js/app.js
# أو
npm run build # إنتاج
```

> القوالب في: `backend/templates` — وملفات الـRTL في: `backend/static/css/admin-rtl.css`
