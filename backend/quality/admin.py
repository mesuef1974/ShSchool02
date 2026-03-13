from django.contrib import admin
from .models import (
    QualityCommittee, 
    QualityDomain, 
    QualityTarget, 
    QualityIndicator, 
    OperationalPlanItem
)

@admin.register(QualityCommittee)
class QualityCommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    filter_horizontal = ('members',)

class QualityTargetInline(admin.TabularInline):
    model = QualityTarget
    extra = 1

@admin.register(QualityDomain)
class QualityDomainAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [QualityTargetInline]

class QualityIndicatorInline(admin.TabularInline):
    model = QualityIndicator
    extra = 1

@admin.register(QualityTarget)
class QualityTargetAdmin(admin.ModelAdmin):
    list_display = ('number', 'description', 'domain')
    list_filter = ('domain',)
    search_fields = ('number', 'description')
    inlines = [QualityIndicatorInline]

@admin.register(QualityIndicator)
class QualityIndicatorAdmin(admin.ModelAdmin):
    list_display = ('number', 'description', 'target')
    list_filter = ('target__domain',)
    search_fields = ('number', 'description')

@admin.register(OperationalPlanItem)
class OperationalPlanItemAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'indicator', 'executor', 'date_range', 'operational_status')
    list_filter = ('operational_status', 'executor_committee', 'evaluator_committee', 'indicator__target__domain')
    search_fields = ('procedure', 'procedure_no', 'indicator__description')
    
    fieldsets = (
        ('1. الهيكلية والإجراء', {
            'fields': ('indicator', ('procedure_no', 'procedure'))
        }),
        ('2. المسؤولية والفرق', {
            'fields': ('executor', 'executor_committee', 'evaluator_committee')
        }),
        ('3. الجدول الزمني والمتابعة', {
            'fields': ('date_range', 'follow_up', 'comments')
        }),
        ('4. الأدلة والتقييم', {
            'fields': ('evidence_type', 'evidence_source_employee', 'evidence_source_file', 'evaluation', 'evaluation_notes')
        }),
        ('5. الحالة', {
            'fields': ('operational_status',)
        }),
    )

    autocomplete_fields = ['indicator', 'executor', 'executor_committee', 'evaluator_committee', 'evidence_source_employee']
    list_per_page = 25
