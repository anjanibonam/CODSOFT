import random

def get_user_input(message):
    """Prompts the user for input until a valid choice is received.

    Args:
        message: The message to display to the user.

    Returns:
        str: The user's valid choice.
    """
    while True:
        choice = input(message).lower()
        valid_options = ["rock", "paper", "scissors"]
        if choice in valid_options:
            return choice
        else:
            print("Invalid selection. Please choose from", ", ".join(valid_options))

def determine_outcome(user_choice, computer_choice):
    """Compares user and computer choices to determine the winner.

    Args:
        user_choice: The user's choice.
        computer_choice: The computer's choice.

    Returns:
        str: "Win", "Loss", or "Tie" depending on the winner.
    """
    winning_combos = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if user_choice == computer_choice:
        return "Tie"

    return "Win" if winning_combos[user_choice] == computer_choice else "Loss"

def play_game():
    """Runs the main game loop."""
    user_wins = 0
    computer_wins = 0

    while True:
        print("Welcome to Rock-Paper-Scissors!")

        user_choice = get_user_input("Enter your choice (rock, paper, scissors): ")

        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = determine_outcome(user_choice, computer_choice)
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        if result == "Win":
            print("You are victorious!")
            user_wins += 1
        elif result == "Loss":
            print("You were defeated.")
            computer_wins += 1
        else:
            print("It's a tie!")

        print(f"Your wins: {user_wins}, Computer wins: {computer_wins}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes" and play_again != "no":
            print("Invalid selection. Please enter 'yes' or 'no'.")
            continue
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
