from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    """
    Custom User model for Shahania School System.
    Extends Django's AbstractUser to allow future customization.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Additional fields can be added here
    is_teacher = models.BooleanField(default=False, verbose_name="معلم")
    is_student = models.BooleanField(default=False, verbose_name="طالب")
    is_parent = models.BooleanField(default=False, verbose_name="ولي أمر")
    
    # National ID is crucial for integration
    national_id = models.CharField(max_length=32, unique=True, null=True, blank=True, verbose_name="الرقم الشخصي")

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username
