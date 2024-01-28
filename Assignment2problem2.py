# Problem #2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    if num2 == 0:
        print("Error: Cannot Divide By Zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operator.")
    result = None

if result != None:
    print(num1, operator, num2, "=", result)

