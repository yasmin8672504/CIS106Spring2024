# Problem #2
attempts = 3

while attempts > 0:
    num = int(input("Enter a number between 10 and 20: "))
    if num < 10 or num > 20:
        print("Number not accepted. You have", attempts - 1, "more attempts.")
        attempts -= 1
    else:
        print("Numbers from 0 to", num, ":")
        for i in range(num + 1):
            print(i)
        break

if attempts == 0:
    print("Maximum attempts exceeded. Ending the program.")
