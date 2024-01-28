# Problem #1
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if pow(side1, 2) == pow(side2, 2) + pow(side3, 2) or pow(side2, 2) == pow(side1, 2) + pow(side3, 2) or pow(side3, 2) == pow(side1, 2) + pow(side2, 2):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
