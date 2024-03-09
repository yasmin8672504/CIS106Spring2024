# Assignment 8 / Problem 4

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}

set3 = set()

for element in set1:
    if element in set2:
        set3.add(element)

print("Set 1:", set1, "\n")
print("Set 2:", set2, "\n")
print("New set 3:", set3, "\n")