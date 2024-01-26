marks = int(input("enter marks: "))
if marks >= 85:
    grades = 'A'
elif marks <= 84 and marks >= 60:
    grades = 'B'
elif marks <= 59 and marks >= 40:
    grades = 'C'
elif marks <= 39 and marks >= 30:
    grades = 'D'
else: 
    grades = 'E'
print (grades)