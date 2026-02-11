"""
PDF generation module for life calendar.
Based on create-pdf.py, adapted for Django integration.
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from math import ceil, sqrt
from io import BytesIO
from datetime import date


def create_life_calendar_pdf(birth_date, estimated_death_date, filename=None):
    """
    Create a PDF with circles representing each day of life.
    Each page represents one year with 365 circles numbered by day.
    
    Args:
        birth_date: datetime.date object for birth date
        estimated_death_date: datetime.date object for estimated death date
        filename: Optional filename. If None, returns BytesIO object
    
    Returns:
        BytesIO object containing PDF data, or saves to filename if provided
    """
    # Calculate total years
    total_days = (estimated_death_date - birth_date).days
    total_years = ceil(total_days / 365.25)
    
    # Create PDF in memory or file
    if filename:
        pdf_buffer = open(filename, 'wb')
    else:
        pdf_buffer = BytesIO()
    
    width, height = A4
    c = canvas.Canvas(pdf_buffer, pagesize=A4)
    
    circles_per_page = 365
    margin = 40
    circle_radius = 12
    
    for year in range(1, total_years + 1):
        # Write year at top of page
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - margin / 2, f"Year {year}")
        
        # Calculate grid layout for 365 circles
        cols = int(sqrt(circles_per_page))
        rows = ceil(circles_per_page / cols)
        spacing_x = (width - 2 * margin) / (cols - 1)
        spacing_y = (height - 2 * margin - 30) / (rows - 1)  # 30 for year header space
        
        count = 1
        for r in range(rows):
            for c_index in range(cols):
                if count > circles_per_page:
                    break
                x = margin + c_index * spacing_x
                y = height - margin - 30 - r * spacing_y
                c.circle(x, y, circle_radius)
                
                # Write day number inside circle
                c.setFont("Helvetica", 6)
                c.drawCentredString(x, y - 2, str(count))
                count += 1
        
        c.showPage()  # Next page
    
    c.save()
    
    if filename:
        pdf_buffer.close()
        return None
    else:
        pdf_buffer.seek(0)
        return pdf_buffer
