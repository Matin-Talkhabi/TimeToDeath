"""
Lifespan calculation module based on the formula from base.txt

This module implements the lifespan estimation formula:
Estimated Age = Base Age + Σ(Factor Effect × Weight)

Factors:
- Exercise: 0.2 weight
- Smoking: 0.25 weight
- BMI: 0.15 weight
- Diet: 0.15 weight
- Alcohol: 0.1 weight
- Health Metrics: 0.15 weight
"""


def calculate_exercise_score(exercise_minutes_per_week):
    """
    Calculate exercise score based on weekly minutes.
    
    ≥ 150 minutes/week → +5
    75-150 minutes → +3
    0-75 minutes → 0
    """
    if exercise_minutes_per_week >= 150:
        return 5
    elif exercise_minutes_per_week >= 75:
        return 3
    else:
        return 0


def calculate_smoking_score(smoking_status):
    """
    Calculate smoking score.
    
    Daily ≥ 1 pack → -10
    Occasional → -5
    None → 0
    """
    smoking_status = smoking_status.lower().strip()
    if smoking_status in ['daily', 'روزانه']:
        return -10
    elif smoking_status in ['occasional', 'sometimes', 'گاهی']:
        return -5
    else:
        return 0


def calculate_bmi_score(weight_kg, height_cm):
    """
    Calculate BMI score.
    
    18.5–24.9 → +2
    25–29.9 → 0
    ≥ 30 or <18.5 → -2
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    if 18.5 <= bmi <= 24.9:
        return 2
    elif 25 <= bmi <= 29.9:
        return 0
    else:
        return -2


def calculate_diet_score(diet_quality):
    """
    Calculate diet score.
    
    Healthy → +2
    Moderate → 0
    Unhealthy → -2
    """
    diet_quality = diet_quality.lower().strip()
    if diet_quality in ['healthy', 'سالم']:
        return 2
    elif diet_quality in ['moderate', 'متوسط']:
        return 0
    else:
        return -2


def calculate_alcohol_score(alcohol_consumption):
    """
    Calculate alcohol score.
    
    Heavy consumption → -3
    Light/None → 0
    """
    alcohol_consumption = alcohol_consumption.lower().strip()
    if alcohol_consumption in ['heavy', 'high', 'زیاد']:
        return -3
    else:
        return 0


def calculate_health_score(has_health_issues):
    """
    Calculate health metrics score.
    
    All normal → +3
    One abnormal → 0
    Multiple abnormal → -5
    """
    if isinstance(has_health_issues, bool):
        return 3 if not has_health_issues else -5
    
    has_health_issues = str(has_health_issues).lower().strip()
    if has_health_issues in ['no', 'false', 'none', 'خیر']:
        return 3
    elif has_health_issues in ['yes', 'true', 'multiple', 'بله']:
        return -5
    else:
        return 0


def calculate_lifespan(
    base_age=75,
    exercise_minutes_per_week=0,
    smoking_status='none',
    weight_kg=70,
    height_cm=170,
    diet_quality='moderate',
    alcohol_consumption='none',
    has_health_issues=False
):
    """
    Calculate estimated lifespan using the weighted formula.
    
    Formula:
    Estimated Age = Base Age + 0.2×Exercise + 0.25×Smoking + 0.15×BMI 
                     + 0.15×Diet + 0.1×Alcohol + 0.15×Health
    
    Args:
        base_age: Base life expectancy (default 75)
        exercise_minutes_per_week: Weekly exercise minutes
        smoking_status: 'none', 'occasional', 'daily'
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters
        diet_quality: 'healthy', 'moderate', 'unhealthy'
        alcohol_consumption: 'none', 'light', 'heavy'
        has_health_issues: Boolean or string indicating health issues
    
    Returns:
        Estimated lifespan in years (float)
    """
    exercise_score = calculate_exercise_score(exercise_minutes_per_week)
    smoking_score = calculate_smoking_score(smoking_status)
    bmi_score = calculate_bmi_score(weight_kg, height_cm)
    diet_score = calculate_diet_score(diet_quality)
    alcohol_score = calculate_alcohol_score(alcohol_consumption)
    health_score = calculate_health_score(has_health_issues)
    
    # Weighted formula
    estimated_age = (
        base_age
        + 0.2 * exercise_score
        + 0.25 * smoking_score
        + 0.15 * bmi_score
        + 0.15 * diet_score
        + 0.1 * alcohol_score
        + 0.15 * health_score
    )
    
    # Ensure minimum age is reasonable (at least 50 years)
    return max(estimated_age, 50)
