from django.db import models
import uuid

# سيتم بناء نماذج وأصول مشتركة (مثل TimeStamped/SoftDelete/UUIDBase) هنا.

class UUIDBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseFormFields(UUIDBase, TimeStamped):
    school_id = models.UUIDField()
    academic_year = models.CharField(max_length=9)
    term = models.CharField(max_length=8)
    form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_by = models.UUIDField()
    status = models.CharField(max_length=24, default='draft')

    class Meta:
        abstract = True
