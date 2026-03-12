from django.db import models
from backend.common.models import BaseFormFields

class Subject(BaseFormFields):
    code = models.CharField(max_length=32, unique=True)
    name_ar = models.CharField(max_length=128)

class ClassRoom(BaseFormFields):
    school = models.ForeignKey('students.School', on_delete=models.CASCADE)
    year = models.ForeignKey('students.AcademicYear', on_delete=models.CASCADE)
    grade = models.CharField(max_length=16)
    section = models.CharField(max_length=8)
    capacity = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('school', 'year', 'grade', 'section')

class Teacher(BaseFormFields):
    full_name_ar = models.CharField(max_length=128)
    phone = models.CharField(max_length=32, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)

class TeachingAssignment(BaseFormFields):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject', 'class_room')
