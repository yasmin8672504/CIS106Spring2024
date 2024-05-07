import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    # Dictionary to map choices to their index
    choices = {"Rock": 0, "Paper": 1, "Scissors": 2}
    
    # Get computer's choice
    computer_choice = random.choice(list(choices.keys()))
    
    # Determine the winner
    user_index = choices[user_choice]
    computer_index = choices[computer_choice]
    result = (user_index - computer_index) % 3
    
    # Update the result label
    if result == 0:
        result_label.config(text=f"Computer chose {computer_choice}. It's a tie!")
    elif result == 1:
        result_label.config(text=f"Computer chose {computer_choice}. You win!")
    else:
        result_label.config(text=f"Computer chose {computer_choice}. Computer wins!")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create widgets
title_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors!")
instruction_label = tk.Label(root, text="Select your choice:")
choices = ["Rock", "Paper", "Scissors"]
choice_var = tk.StringVar(root)
choice_var.set(choices[0])  # Default choice
choice_menu = tk.OptionMenu(root, choice_var, *choices)
play_button = tk.Button(root, text="Play", command=lambda: determine_winner(choice_var.get()))
result_label = tk.Label(root, text="")

# Place widgets in the window
title_label.pack()
instruction_label.pack()
choice_menu.pack()
play_button.pack()
result_label.pack()

# Run the main event loop
root.mainloop()
