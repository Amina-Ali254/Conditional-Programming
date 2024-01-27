# Create grading calculation using conditional programming, example 'A' , 'A-' etc.?
# Defined Calculations
def calculate_grade(marks):
    if marks >= 90:
        if marks >= 97:
            return 'A+'
        elif marks >= 93:
            return 'A'
        else:
            return 'A-'
    elif marks >= 80:
        if marks >= 87:
            return 'B+'
        elif marks >= 83:
            return 'B'
        else:
            return 'B-'
    elif marks >= 70:
        if marks >= 77:
            return 'C+'
        elif marks >= 73:
            return 'C'
        else:
            return 'C-'
    elif marks >= 60:
        if marks >= 67:
            return 'D+'
        elif marks >= 63:
            return 'D'
        else:
            return 'D-'
    else:
        return 'F'

# Halima's scores
english_marks = 90
math_marks = 70
science_marks = 65

# Calculate grades
english_grade = calculate_grade(english_marks)
math_grade = calculate_grade(math_marks)
science_grade = calculate_grade(science_marks)

# Print Halima's grades
print(f"Halima's Grades:\nEnglish: {english_grade}\nMath: {math_grade}\nScience: {science_grade}")
