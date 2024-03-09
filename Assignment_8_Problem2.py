# Assignment 8 / Problem 2

numbers = []

for i in range(1, 21):
    number = float(input(f"Enter number {i}: "))
    numbers.append(number)

lowest = min(numbers)
highest = max(numbers)

total = sum(numbers)

average = total / len(numbers)

print(f"lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total of the numbers: {total}")
print(f"Average of the numbers: {average}")

