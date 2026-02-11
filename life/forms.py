from django import forms
from datetime import date


class LifeCalculationForm(forms.Form):
    """
    Form for collecting user information to calculate lifespan.
    """
    # Basic info
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'max': date.today().isoformat()
        }),
        label='Date of Birth',
        help_text='Select your date of birth'
    )
    
    gender = forms.ChoiceField(
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }),
        label='Gender'
    )
    
    # Lifestyle factors
    exercise_minutes_per_week = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'min': '0',
            'placeholder': 'e.g., 150'
        }),
        label='Exercise (minutes per week)',
        help_text='How many minutes of exercise do you do per week?',
        min_value=0,
        initial=0
    )
    
    smoking_status = forms.ChoiceField(
        choices=[
            ('none', 'None'),
            ('occasional', 'Occasional'),
            ('daily', 'Daily'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }),
        label='Smoking Status',
        initial='none'
    )
    
    weight_kg = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'min': '1',
            'step': '0.1',
            'placeholder': 'e.g., 70'
        }),
        label='Weight (kg)',
        min_value=1
    )
    
    height_cm = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none',
            'min': '50',
            'step': '0.1',
            'placeholder': 'e.g., 170'
        }),
        label='Height (cm)',
        min_value=50
    )
    
    diet_quality = forms.ChoiceField(
        choices=[
            ('healthy', 'Healthy'),
            ('moderate', 'Moderate'),
            ('unhealthy', 'Unhealthy'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }),
        label='Diet Quality',
        initial='moderate'
    )
    
    alcohol_consumption = forms.ChoiceField(
        choices=[
            ('none', 'None'),
            ('light', 'Light'),
            ('heavy', 'Heavy'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }),
        label='Alcohol Consumption',
        initial='none'
    )
    
    has_health_issues = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-600 focus:ring-2 focus:ring-blue-500'
        }),
        label='Do you have health issues (high blood pressure, diabetes, high cholesterol)?',
        initial=False
    )
    
    def clean_date_of_birth(self):
        """Ensure date of birth is in the past."""
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob >= date.today():
            raise forms.ValidationError("Date of birth must be in the past.")
        return dob
