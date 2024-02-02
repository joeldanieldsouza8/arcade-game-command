import argparse
import random
import sys
from typing import Callable, Optional


def counter_factory() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def main(player_choice_input: Optional[int]) -> None:
    player_wins: Callable[[], int] = counter_factory()
    computer_wins: Callable[[], int] = counter_factory()
    ties: Callable[[], int] = counter_factory()

    boolean_flag: bool = True

    while boolean_flag:
        # Convert user input to integer
        try:
            player: int
            
            if player_choice_input is not None:
                player = int(player_choice_input)
            else:
                player_input = input(
                    "👋 Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n"
                )
                player = int(player_input)
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 3.")
            continue

        # Check if user input is valid
        if player > 3 or player < 1:
            print("❌ Invalid input. Please enter a number between 1 and 3.")
            continue

        player_choice: str = get_choice(player)

        # Generate random number
        computer: int = random.randint(1, 3)
        computer_choice: str = get_choice(computer)

        # Print user and computer choices
        print(f"\n👨 You chose {player_choice}.")
        print(f"💻 The computer chose {computer_choice}.\n")

        # Compare user and computer choices
        result = check_winner(player, computer)
        if result == "tie":
            ties()
        elif result == "win":
            player_wins()
        elif result == "lose":
            computer_wins()

        # Ask user if they want to play again
        play_again: str = input("\n😁 Would you like to play again? (y/n)\n\n")
        if play_again.lower() != "y":
            print(f"\nFinal score:")
            print(f"👨 You won {player_wins()} times.")
            print(f"💻 The computer won {computer_wins()} times.")
            print(f"🪢 There were {ties()} ties.")
            boolean_flag = False
        else:
            player_choice_input = None

    # Print goodbye message
    print("\n✅ Thanks for playing!")


def get_choice(number: int) -> str:
    """Convert a number (1, 2, or 3) into the corresponding choice of Rock, Paper, or Scissors."""
    match number:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            print("❌ Invalid input. Please enter a number between 1 and 3.")
            sys.exit()


def check_winner(player: int, computer: int) -> str:
    """Compare user and computer choices and print the outcome."""
    if (player, computer) in ((1, 1), (2, 2), (3, 3)):
        print("🪢 It's a tie!")
        return "tie"
    elif (player, computer) in ((1, 3), (2, 1), (3, 2)):
        print("😍 You win!")
        return "win"
    elif (player, computer) in ((1, 2), (2, 3), (3, 1)):
        print("😭 You lose!")
        return "lose"

    return ""  # Add a default return statement


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Play Rock-Paper-Scissors.")

#     argument_number: str = "-n"
#     argument_number_long: str = "--number"
#     number_required: bool = True
#     number_help: str = "Enter 1 for Rock, 2 for Paper, 3 for Scissors."

#     parser.add_argument(argument_number, argument_number_long,
#                         required=number_required, help=number_help, type=int)
    
#     args: argparse.Namespace = parser.parse_args()
#     main(player_choice_input=args.number)
