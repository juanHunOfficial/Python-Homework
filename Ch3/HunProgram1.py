#Author: Hun, Juan P.


side_a = int(input("Enter the value of side A: "))
side_b = int(input("Enter the value of side B: "))
side_c = int(input("Enter the value of side C: "))

if side_a == side_b and side_b == side_c:
    print("The triangle is equilateral")
else:
    print("This is not an equilateral triangle")