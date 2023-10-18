import random

# Define the game options
options = ["Rock", "Paper","Scissors"]

# Function to get the user's choice
def get_user_choice():
    while True:
        print("Enter your choice (Rock, Paper, Scissors):")
        user_choice = input().capitalize()
        if user_choice in options:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(options)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
