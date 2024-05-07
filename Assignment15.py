import tkinter as tk
import random

# This is a simple "Rock, Paper, Scissors" game.
# The game allows the user to select one of the three options: rock, paper, or scissors, by choosing from a dropdown menu. 
# Once the user makes their choice and clicks the "Play" button, the computer randomly selects one of the options as well. 
# The winner is determined based on the classic rules of the game: Rock beats scissors, Scissors beats paper, and Paper beats rock
# The winner is displayed in the result label below the play button. If it's a tie, the result label will indicate a tie.
# The user can keep playing by pressing play.
# The game ends when the window is closed. 

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
