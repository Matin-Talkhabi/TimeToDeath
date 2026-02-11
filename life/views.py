from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from datetime import date, timedelta
import secrets
from .forms import LifeCalculationForm
from .models import LifeCalculation
from .lifespan_calculator import calculate_lifespan
from .pdf_generator import create_life_calendar_pdf


def index(request):
    """
    Main page with form to collect user information.
    """
    if request.method == 'POST':
        form = LifeCalculationForm(request.POST)
        if form.is_valid():
            # Calculate lifespan
            dob = form.cleaned_data['date_of_birth']
            estimated_years = calculate_lifespan(
                base_age=75,
                exercise_minutes_per_week=form.cleaned_data['exercise_minutes_per_week'],
                smoking_status=form.cleaned_data['smoking_status'],
                weight_kg=form.cleaned_data['weight_kg'],
                height_cm=form.cleaned_data['height_cm'],
                diet_quality=form.cleaned_data['diet_quality'],
                alcohol_consumption=form.cleaned_data['alcohol_consumption'],
                has_health_issues=form.cleaned_data['has_health_issues']
            )
            
            # Create unique ID for sharing
            unique_id = secrets.token_urlsafe(16)
            
            # Save calculation
            calculation = LifeCalculation.objects.create(
                date_of_birth=dob,
                gender=form.cleaned_data['gender'],
                exercise_minutes_per_week=form.cleaned_data['exercise_minutes_per_week'],
                smoking_status=form.cleaned_data['smoking_status'],
                weight_kg=form.cleaned_data['weight_kg'],
                height_cm=form.cleaned_data['height_cm'],
                diet_quality=form.cleaned_data['diet_quality'],
                alcohol_consumption=form.cleaned_data['alcohol_consumption'],
                has_health_issues=form.cleaned_data['has_health_issues'],
                estimated_lifespan_years=estimated_years,
                unique_id=unique_id
            )
            
            # Redirect to results page
            return redirect('life:results', unique_id=unique_id)
    else:
        form = LifeCalculationForm()
    
    return render(request, 'life/index.html', {'form': form})


def results(request, unique_id):
    """
    Results page showing elapsed and remaining life with timers.
    """
    calculation = get_object_or_404(LifeCalculation, unique_id=unique_id)
    
    # Calculate dates
    birth_date = calculation.date_of_birth
    today = date.today()
    estimated_death_date = birth_date + timedelta(days=int(calculation.estimated_lifespan_years * 365.25))
    
    # Calculate elapsed and remaining time
    elapsed_delta = today - birth_date
    remaining_delta = estimated_death_date - today
    
    # Convert to total seconds for JavaScript timer
    elapsed_seconds = int(elapsed_delta.total_seconds())
    remaining_seconds = max(0, int(remaining_delta.total_seconds()))
    
    # Calculate breakdown for display
    elapsed_years = elapsed_delta.days // 365
    elapsed_months = (elapsed_delta.days % 365) // 30
    elapsed_days = elapsed_delta.days % 30
    
    remaining_years = remaining_delta.days // 365
    remaining_months = (remaining_delta.days % 365) // 30
    remaining_days = remaining_delta.days % 30
    
    # Calculate percentage of life lived
    total_lifespan_days = (estimated_death_date - birth_date).days
    life_percentage = min(100, (elapsed_delta.days / total_lifespan_days * 100)) if total_lifespan_days > 0 else 0
    
    context = {
        'calculation': calculation,
        'birth_date': birth_date,
        'estimated_death_date': estimated_death_date,
        'today': today,
        'elapsed_seconds': elapsed_seconds,
        'remaining_seconds': remaining_seconds,
        'elapsed_years': elapsed_years,
        'elapsed_months': elapsed_months,
        'elapsed_days': elapsed_days,
        'remaining_years': remaining_years,
        'remaining_months': remaining_months,
        'remaining_days': remaining_days,
        'life_percentage': round(life_percentage, 2),
        'share_url': request.build_absolute_uri(request.path),
    }
    
    return render(request, 'life/results.html', context)


def generate_pdf(request, unique_id):
    """
    Generate and download PDF for the life calendar.
    """
    calculation = get_object_or_404(LifeCalculation, unique_id=unique_id)
    
    birth_date = calculation.date_of_birth
    estimated_death_date = birth_date + timedelta(days=int(calculation.estimated_lifespan_years * 365.25))
    
    # Generate PDF
    pdf_buffer = create_life_calendar_pdf(birth_date, estimated_death_date)
    
    if pdf_buffer is None:
        raise Http404("PDF generation failed")
    
    # Create response
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="life_calendar_{unique_id[:8]}.pdf"'
    
    return response
