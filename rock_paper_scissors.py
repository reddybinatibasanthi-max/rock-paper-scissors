import random  # Imports the random module to generate random choices


def get_choices():  # Gets the player's and computer's choices
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()  # Takes input, ignores case and extra spaces
    options = ["rock", "paper", "scissors"]  # Stores all possible choices
    computer_choice = random.choice(options)  # Randomly selects one choice for the computer
    return {"player": player_choice, "computer": computer_choice}  # Returns both choices in a dictionary


def check_win(player, computer):  # Checks who wins
    if player not in ["rock", "paper", "scissors"]:  # Validates the player's input
        return "Invalid choice! Please enter rock, paper, or scissors."

    print(f"You chose {player}, Computer chose {computer}")  # Displays both choices

    if player == computer:  # Checks if both choices are the same
        return "It's a Tie!"

    elif player == "rock":  # Player selected rock
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:  # Computer selected paper
            return "Paper covers rock! You lose."

    elif player == "paper":  # Player selected paper
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:  # Computer selected scissors
            return "Scissors cuts paper! You lose."

    elif player == "scissors":  # Player selected scissors
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:  # Computer selected rock
            return "Rock smashes scissors! You lose."


def main():  # Runs the game
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)


if __name__ == "__main__":  # Runs main() only when this file is executed directly
    main()
