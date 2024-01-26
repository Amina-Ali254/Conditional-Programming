marks = int(input('enter marks:'))
if marks >= 90:
    grade = 'A'
elif marks <= 89 and marks >= 70:
    grade = 'B'
elif marks <= 69 and marks >= 50:
    grade = 'C'
elif marks <= 49 and marks >= 30:
    grade = 'D'
else:
    grade = 'E'
print (grade)