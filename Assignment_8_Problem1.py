
# Assignment 8 / Problem 1

rainfall = []

for month in range (1, 13):
    rainfall_entry = float(input(f"Enter rainfall for month {month}:  "))
    rainfall.append(rainfall_entry)

total_rainfall = sum(rainfall)

average_rainfall = total_rainfall / len(rainfall)

max_rainfall_month = rainfall.index(max(rainfall)) + 1
min_rainfall_month = rainfall.index(min(rainfall)) + 1 

print(f"Total rainfall for the year: {total_rainfall}")
print(f"Average monthly rainfall: {average_rainfall}")
print(f"Month with the highest rainfall: {max_rainfall_month}")
print(f"Month with the lowest rainfall: {min_rainfall_month}")