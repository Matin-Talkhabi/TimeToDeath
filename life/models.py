from django.db import models
from django.utils import timezone


class LifeCalculation(models.Model):
    """
    Model to store user's life calculation data.
    This allows users to share their results via a unique URL.
    """
    # Basic info
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    
    # Lifestyle factors
    exercise_minutes_per_week = models.IntegerField(default=0)
    smoking_status = models.CharField(max_length=20, choices=[
        ('none', 'None'),
        ('occasional', 'Occasional'),
        ('daily', 'Daily'),
    ], default='none')
    weight_kg = models.FloatField()
    height_cm = models.FloatField()
    diet_quality = models.CharField(max_length=20, choices=[
        ('healthy', 'Healthy'),
        ('moderate', 'Moderate'),
        ('unhealthy', 'Unhealthy'),
    ], default='moderate')
    alcohol_consumption = models.CharField(max_length=20, choices=[
        ('none', 'None'),
        ('light', 'Light'),
        ('heavy', 'Heavy'),
    ], default='none')
    has_health_issues = models.BooleanField(default=False)
    
    # Calculated values
    estimated_lifespan_years = models.FloatField()
    base_age = models.FloatField(default=75)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=32, unique=True, db_index=True)
    
    def __str__(self):
        return f"Life Calculation - {self.date_of_birth} - {self.estimated_lifespan_years} years"
    
    class Meta:
        ordering = ['-created_at']
