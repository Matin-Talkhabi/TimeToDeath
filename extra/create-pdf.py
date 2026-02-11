from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from math import ceil, sqrt

def create_circles_pdf(years, filename="circles.pdf"):
    width, height = A4
    c = canvas.Canvas(filename, pagesize=A4)

    circles_per_page = 365
    margin = 40
    circle_radius = 12  # کمی بزرگتر برای جا شدن شماره داخل دایره

    for year in range(1, years + 1):
        # نوشتن سال بالای صفحه
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - margin / 2, f"Year {year}")

        # محاسبه تعداد ردیف و ستون برای 365 دایره
        cols = int(sqrt(circles_per_page))
        rows = ceil(circles_per_page / cols)
        spacing_x = (width - 2 * margin) / (cols - 1)
        spacing_y = (height - 2 * margin - 30) / (rows - 1)  # 30 برای فضای بالای سال

        count = 1
        for r in range(rows):
            for c_index in range(cols):
                if count > circles_per_page:
                    break
                x = margin + c_index * spacing_x
                y = height - margin - 30 - r * spacing_y
                c.circle(x, y, circle_radius)

                # نوشتن شماره داخل دایره
                c.setFont("Helvetica", 6)
                c.drawCentredString(x, y - 2, str(count))  # کمی پایین‌تر برای وسط شدن
                count += 1

        c.showPage()  # صفحه بعدی

    c.save()
    print(f"PDF ساخته شد: {filename}")

# مثال استفاده:
create_circles_pdf()  # دو سال
