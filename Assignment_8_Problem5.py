# Assignment 8 / Problem 5

import random

# Dictionary containing states and their capitals
states_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# Initialize counters for correct and incorrect responses
correct_answers = 0
incorrect_answers = 0


# Quiz the user
print("Welcome to the Capital Quiz!")
print("Enter the capital of each state. Type 'exit' to quit.")

states = list(states_capitals.keys())
random.shuffle(states)


# Loop through each state in the dictionary
for state in states:
    # Display the state name
    print(f"\nWhat is the capital of {state} ?")
    # Get the user's input
    user_input = input("Enter the capital: ")
    
    user_input_lower = user_input.lower()
    correct_capital_lower = states_capitals[state].lower()

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        break
    
    # Check if the user's input matches the correct capital
    if user_input_lower == correct_capital_lower:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The capital of {state} is {states_capitals[state]}.")
        incorrect_answers += 1

# Display the final score
print("\nQuiz Summary:")
print(f"Correct answers: {correct_answers} ")
print(f"Incorrect answers: {incorrect_answers} ")
