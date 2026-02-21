def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"

    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"