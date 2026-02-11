from errno import ESTALE


def estimate_life(base_age=75):
    print("تخمین عمر بر اساس سبک زندگی و سلامت فرد\n")

    # ورزش
    exercise = input("ورزش در هفته چند دقیقه انجام می‌دهید؟ (عدد به دقیقه): ")
    exercise = int(exercise)
    if exercise >= 150:
        exercise_score = 5
    elif exercise >= 75:
        exercise_score = 3
    else:
        exercise_score = 0

    # سیگار
    smoking = input("سیگار می‌کشید؟ (هیچ/گاهی/روزانه): ").strip().lower()
    if smoking == "روزانه":
        smoking_score = -10
    elif smoking == "گاهی":
        smoking_score = -5
    else:
        smoking_score = 0

    # BMI
    weight = float(input("وزن شما (کیلوگرم): "))
    height = float(input("قد شما (سانتی‌متر): "))
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    if 18.5 <= bmi <= 24.9:
        bmi_score = 2
    elif 25 <= bmi <= 29.9:
        bmi_score = 0
    else:
        bmi_score = -2

    # رژیم غذایی
    diet = input("رژیم غذایی شما چگونه است؟ (سالم/متوسط/ناسالم): ").strip().lower()
    if diet == "سالم":
        diet_score = 2
    elif diet == "متوسط":
        diet_score = 0
    else:
        diet_score = -2

    # الکل
    alcohol = input("مصرف الکل دارید؟ (زیاد/کم/هیچ): ").strip().lower()
    if alcohol == "زیاد":
        alcohol_score = -3
    else:
        alcohol_score = 0

    # فشار خون و کلسترول و قند (ساده)
    health = input("آیا فشار خون یا قند یا کلسترول غیر نرمال دارید؟ (بله/خیر): ").strip().lower()
    if health == "خیر":
        health_score = 3
    elif health == "بله":
        health_score = -5
    else:
        health_score = 0

    # وزن‌دهی فاکتورها
    estimated_age = base_age \
        + 0.2 * exercise_score \
        + 0.25 * smoking_score \
        + 0.15 * bmi_score \
        + 0.15 * diet_score \
        + 0.1 * alcohol_score \
        + 0.15 * health_score

    return estimated_age


    


# اجرا
print(estimate_life())
