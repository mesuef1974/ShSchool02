from django.contrib import admin
from .models import School, AcademicYear, Term, Guardian, Student, Enrollment

admin.site.register(School)
admin.site.register(AcademicYear)
admin.site.register(Term)
admin.site.register(Guardian)
admin.site.register(Student)
admin.site.register(Enrollment)
