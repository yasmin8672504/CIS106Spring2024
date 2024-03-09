# Assignment 8 / Problem 3


# Defining a tuple containing client information
client1 = ("Jazlene", "Gonzalez", "25")

# Print the tuple
print("Client tuple:", client1)

# Print individual elements of the tuple
print("First name: ", client1[0])
print("Last name: ", client1[1])
print("Age: ", client1[2])

try:
# Trying to modify tuple (should raise an error)
    client1[2] = 35
    print(client1[2])

except TypeError as e:
    print("Error:", e)