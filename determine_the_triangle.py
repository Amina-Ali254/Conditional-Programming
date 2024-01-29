side1 = int(input("enter side1: "))
side2 = int(input ("enter side2: "))
side3 = int(input("enter side3: "))
if side1 == side2 == side3:
    print("it is an equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("it is an isosceles triangle")
else:
    print("it is a scalene triangle")