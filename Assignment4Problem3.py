# Problem #3
favorite_names = ["Andrew", "Bob", "Chrissy", "David", "Emily", "Fatima", "Grant", "Harper", "Iris", "Jazlene"]

while True:
    name = input("Enter a name: ").capitalize()
    if name in favorite_names:
        print(name, "is on the favorite names list!")
        break
    else:
        print("Sorry, that name is not in the list. Please try again.")
