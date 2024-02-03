# Problem #2
def perform_operation(num1, num2, operation_code):
    if operation_code == 'A':
        result = num1 + num2
    elif operation_code == 'S':
        result = num1 - num2
    elif operation_code == 'M':
        result = num1 * num2
    elif operation_code == 'D':
        if num2 == 0:
            result = -999
        else:
            result = num1 / num2
    else:
        result = None

    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation_code = input("Enter the operation code (A for addition, S for subtraction, M for multiplication, D for division): ").upper()

result = perform_operation(num1, num2, operation_code)

print("Numbers:", num1, "and", num2)
print("Operation code:", operation_code)
if result == -999:
    print( result, "Cannot divide by zero")
else:
    print("Result:", result)
