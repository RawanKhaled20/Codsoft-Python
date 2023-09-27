"""Author: Rawan Khaled  https://github.com/RawanKhaled20/Codsoft-Python.git"""

import tkinter as tk
import random

# Initialize scores
user_score_value = 0
computer_score_value = 0

# Function to determine the winner and update scores
def determine_winner(user_choice, computer_choice):
    global user_score_value
    global computer_score_value

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You win!")
        user_score_value += 1
        user_score.set(user_score_value)
    else:
        result_label.config(text="Computer wins!")
        computer_score_value += 1
        computer_score.set(computer_score_value)

# Function to handle user's choice
def choose_option(option):
    user_choice_label.config(text="Your Choice: " + option)
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    computer_choice_label.config(text="Computer's Choice: " + computer_choice)

    result = determine_winner(option, computer_choice)
    result_label.config(text=result)

# Function to reset the game
def play_again():
    global user_score_value
    global computer_score_value

    user_score_value = 0
    computer_score_value = 0

    user_score.set(user_score_value)
    computer_score.set(computer_score_value)

    result_label.config(text="")
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("300x400")
root.configure(bg="skyblue")
# Load and set the icon image
icon_image = tk.PhotoImage(file="rock-paper-scissors.png")  # Replace "icon.png" with the actual image file
root.iconphoto(False, icon_image)

# Labels
user_choice_label = tk.Label(root, text="Your Choice: ", bg="skyblue", pady=20)
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's Choice: ", bg="skyblue")
computer_choice_label.pack()

result_label = tk.Label(root, text="", bg="skyblue")
result_label.pack()

# User Score
user_score = tk.IntVar()
user_score.set(0)
user_score_label = tk.Label(root, text="Your Score: ", bg="skyblue")
user_score_label.pack()
user_score_display = tk.Label(root, textvariable=user_score, bg="skyblue")
user_score_display.pack()

# Computer Score
computer_score = tk.IntVar()
computer_score.set(0)
computer_score_label = tk.Label(root, text="Computer's Score: ", bg="skyblue")
computer_score_label.pack()
computer_score_display = tk.Label(root, textvariable=computer_score, bg="skyblue")
computer_score_display.pack()

# Create a frame to hold the buttons with padding
button_frame = tk.Frame(root, bg="skyblue", padx=10, pady=10)
button_frame.pack()

# Define a uniform size for all buttons
button_width = 10
button_height = 2

# Buttons
rock_button = tk.Button(button_frame, text="Rock", command=lambda:choose_option("Rock"), width=button_width, height=button_height)
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text="Paper", command= lambda:choose_option("Paper"), width=button_width, height=button_height)
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda:choose_option("Scissors"), width=button_width, height=button_height)
scissors_button.grid(row=0, column=2, padx=5, pady=5)

play_again_button = tk.Button(root, text="Play Again", command= play_again, width=button_width, height=button_height)
play_again_button.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=root.quit, width=button_width, height=button_height)
quit_button.pack()

root.mainloop()








