#Author: Hun, Juan P.

side_a = int(input("Enter the value of side A: "))
side_b = int(input("Enter the value of side B: "))
side_c = int(input("Enter the value of side C: "))

if (side_c ** 2) == (side_b ** 2) + (side_a ** 2):
    print("The triangle is a right triangle")
else:
    print("This is not a right triangle")