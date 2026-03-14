from django.core.management.base import BaseCommand
from apps.core.models import School, Year, Term, Subject
from apps.refdata.models import LookupNationality, LookupAbsenceReason
class Command(BaseCommand):
    help='Load initial reference data'
    def handle(self,*args,**kwargs):
        LookupNationality.objects.get_or_create(code='QA', defaults={'name_ar':'قطري','name_en':'Qatari'})
        LookupAbsenceReason.objects.get_or_create(code='SICK', defaults={'name_ar':'مرض'})
        s,_=School.objects.get_or_create(moehe_code='SHH-001', defaults={'name_ar':'مدرسة الشحانية','name_en':'Shahania School'})
        y,_=Year.objects.get_or_create(school=s, label='2025-2026', start_date='2025-08-15', end_date='2026-06-15')
        Term.objects.get_or_create(year=y, code='T1', start_date='2025-08-15', end_date='2025-11-10')
        Term.objects.get_or_create(year=y, code='T2', start_date='2025-11-25', end_date='2026-03-01')
        for subj in ['الرياضيات','اللغة العربية','اللغة الإنجليزية','العلوم','الفيزياء','الكيمياء']:
            Subject.objects.get_or_create(name_ar=subj)
        self.stdout.write(self.style.SUCCESS('Initial data loaded.'))
