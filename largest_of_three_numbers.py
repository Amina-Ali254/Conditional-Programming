a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))
if a >= b and a >= c:
    print("a is the largest number among three")
elif b >= a and b >= c:
    print ("b is the largeest number among three")
else:
    print("c is the largest number among three")