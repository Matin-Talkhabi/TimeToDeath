from django.contrib import admin
from .models import LifeCalculation


@admin.register(LifeCalculation)
class LifeCalculationAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'gender', 'estimated_lifespan_years', 'created_at', 'unique_id')
    list_filter = ('gender', 'smoking_status', 'diet_quality', 'created_at')
    search_fields = ('unique_id', 'date_of_birth')
    readonly_fields = ('unique_id', 'created_at', 'estimated_lifespan_years')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('date_of_birth', 'gender')
        }),
        ('Lifestyle Factors', {
            'fields': ('exercise_minutes_per_week', 'smoking_status', 'diet_quality', 
                      'alcohol_consumption', 'has_health_issues')
        }),
        ('Physical Information', {
            'fields': ('weight_kg', 'height_cm')
        }),
        ('Results', {
            'fields': ('estimated_lifespan_years', 'base_age')
        }),
        ('Metadata', {
            'fields': ('unique_id', 'created_at')
        }),
    )
