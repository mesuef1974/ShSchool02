from django.contrib import admin
from .models import Subject, ClassRoom, Teacher, TeachingAssignment

admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Teacher)
admin.site.register(TeachingAssignment)
