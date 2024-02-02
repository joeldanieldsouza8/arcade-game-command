import argparse
import random
from typing import Callable


def counter_factory() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def main(player_name: str) -> None:
    player_wins: Callable[[], int] = counter_factory()
    computer_wins: Callable[[], int] = counter_factory()

    boolean_flag: bool = True

    while boolean_flag:
        player_choice_input = input(
            f"\n {player_name}, guess which number I'm thinking of... 1,2, or 3? ")

        # Convert user input to integer
        try:
            player: int = int(player_choice_input)

        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 3.")
            continue

        # Check if user input is valid
        if player not in [1, 2, 3]:
            print("❌ Invalid input. Please enter a number between 1 and 3.")
            continue

        computer: int = random.randint(1, 3)
        computer_choice: str = str(computer)

        print(f"\n {player_name}, you chose {player}.")
        print(f"\n I was thinking about the number {computer_choice}.\n")

        if player == computer:
            print(f"🎉 {player_name}, you guessed correctly! 🎉")
            player_wins()
        else:
            print(f"❌ {player_name}, you guessed incorrectly. 😔")
            computer_wins()

        winning_percentage: float = player_wins() / (player_wins() + computer_wins()) * 100

        print(f"\nYour winning percentage: {winning_percentage:.2f}%")

        play_again: str = input(
            f"\nPlay again, {player_name}?\n Y for Yes or \n Q for Quit\n")

        if play_again.lower() == 'q':
            boolean_flag = False
            
        elif play_again.lower() == 'y':
            continue

        else:
            print("❌ Invalid input. Please enter Y or Q.")
            break

        print("\nGoodbye! 😊")


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Play a game of guess the number against the computer.")

#     argument_name: str = "-n"
#     argument_fullname: str = "--name"
#     name_required: bool = True
#     name_help: str = "Your first name"

#     parser.add_argument(argument_name, argument_fullname,
#                         required=name_required, help=name_help)

#     args: argparse.Namespace = parser.parse_args()
#     main(player_name=args.name)
