# apps/core/templatetags/admin_kpis.py
from django import template
from django.apps import apps as django_apps
from django.utils import timezone

register = template.Library()

def _safe_count(app_label, model_name, filters=None):
    try:
        Model = django_apps.get_model(app_label, model_name)
        qs = Model.objects.all()
        if filters:
            qs = qs.filter(**filters)
        return qs.count()
    except Exception:
        return 0

@register.inclusion_tag("admin/_kpi_bar.html", takes_context=True)
def sh_kpi_bar(context):
    today = timezone.localdate()
    data = {
        "students": _safe_count("people", "Student"),
        "staff":    _safe_count("people", "Staff"),
        "att_today": _safe_count("attendance", "AttendanceRecord", {"date": today}),
        "incidents_today": _safe_count("behavior", "Incident", {"date": today}) or _safe_count("behavior", "BehaviorRecord", {"date": today}),
        "loans_active": _safe_count("library", "Loan", {"returned_at__isnull": True}) or _safe_count("library", "Loan", {"status": "active"}),
    }
    return {"kpi": data}