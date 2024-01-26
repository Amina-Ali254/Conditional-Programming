# How to grade using Python
marks = int(input("enter marks: "))
if marks >= 85:
    grades = 'A'
elif marks <= 84 & marks >= 60:
    grades = 'B'
elif marks <= 59 & marks >= 40:
    grades = 'C'
elif marks <= 39 & marks >= 30:
    grades = 'D'
else: 
    grades = 'E'
print (grades)

# Operator 'NOT'
print (not True)
