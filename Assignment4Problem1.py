# Problem #1
while True:
    num = int(input("Enter a number between 10 and 20: "))
    if num < 10 or num > 20:
        print("Input not accepted. Please try again.")
    else:
        break

print("Numbers from 0 to", num, ":")
for i in range(num + 1):
    print(i)
