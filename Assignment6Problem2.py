# Problem 2

full_name = input("Enter full name (first, middle, last): ")

get_names = full_name.split()

initials_output = '.'.join(name[0].upper() for name in get_names)

print(initials_output)
