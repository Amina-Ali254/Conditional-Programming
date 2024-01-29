a = int(input("enter number 1: "))
operator = input("enter operator(+,-,*,/)")
b = int (input ("enter number 2: "))
if operator == '+':
    print(a + b)
elif operator == '-':
    print (a - b)
elif operator == '*':
    print (a * b)
elif operator == '/':
    print (a / b)
else:
    print('invalid operator')