# Time To Death

A Django web application that estimates your lifespan based on lifestyle and health factors, and displays real-time countdown timers for elapsed and remaining life.

## Features

- **Lifespan Calculation**: Uses a weighted formula based on exercise, smoking, BMI, diet, alcohol consumption, and health metrics
- **Real-time Timers**: Live countdown showing elapsed life (increasing) and remaining life (decreasing)
- **Life Calendar PDF**: Generate a PDF with circles representing each day of your estimated life
- **Share Results**: Share your results with friends via unique URLs
- **Modern UI**: Beautiful dark theme with Tailwind CSS, responsive design

## Requirements

- Python 3.8+
- Django 5.0+
- reportlab (for PDF generation)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd timetodeath
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
timetodeath/
├── life/                    # Main Django app
│   ├── models.py           # LifeCalculation model
│   ├── views.py            # View functions
│   ├── forms.py            # Form definitions
│   ├── urls.py             # URL routing
│   ├── lifespan_calculator.py  # Lifespan calculation logic
│   ├── pdf_generator.py    # PDF generation
│   └── templates/
│       └── life/
│           ├── base.html   # Base template
│           ├── index.html  # Form page
│           └── results.html # Results page
├── timetodeath/            # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Usage

1. **Fill out the form** on the main page with your information:
   - Date of birth
   - Gender
   - Weight and height
   - Exercise minutes per week
   - Smoking status
   - Diet quality
   - Alcohol consumption
   - Health issues

2. **View your results** showing:
   - Elapsed life timer (increasing)
   - Remaining life timer (decreasing)
   - Life progress percentage
   - Summary statistics

3. **Generate PDF** to download a life calendar with circles for each day

4. **Share your results** using the share button

## Lifespan Calculation Formula

The lifespan is calculated using a weighted formula:

```
Estimated Age = Base Age (75) 
    + 0.2 × Exercise Score
    + 0.25 × Smoking Score
    + 0.15 × BMI Score
    + 0.15 × Diet Score
    + 0.1 × Alcohol Score
    + 0.15 × Health Score
```

### Scoring System

- **Exercise**: ≥150 min/week (+5), 75-150 min/week (+3), <75 min/week (0)
- **Smoking**: Daily (-10), Occasional (-5), None (0)
- **BMI**: 18.5-24.9 (+2), 25-29.9 (0), <18.5 or ≥30 (-2)
- **Diet**: Healthy (+2), Moderate (0), Unhealthy (-2)
- **Alcohol**: Heavy (-3), Light/None (0)
- **Health**: All normal (+3), Issues (-5)

## Customization

### Colors

Colors can be easily customized in the templates:
- Main background: `bg-gray-800` (in base.html)
- Elapsed life: Red theme (`from-red-900/50 to-red-800/30`)
- Remaining life: Green theme (`from-green-900/50 to-green-800/30`)

### Base Age

The base age (default: 75) can be adjusted in `life/lifespan_calculator.py` or passed as a parameter.

## Development

### Running Tests

```bash
python manage.py test
```

### Admin Interface

Access the admin interface at `http://127.0.0.1:8000/admin/` after creating a superuser.

## License

This project is open source and available for personal use.

## Developer

**Matin Talkhabi**
- GitHub: [https://github.com/Matin-Talkhabi](https://github.com/Matin-Talkhabi)
- LinkedIn: [https://www.linkedin.com/in/matin-talkhabi/](https://www.linkedin.com/in/matin-talkhabi/)
