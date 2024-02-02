import argparse
import sys
import rps_5
import guess_number


def play_game(name: str = "PlayerOne") -> None:
    """Play a game of Rock, Paper, Scissors or Guess the Number."""
    while True:
        game_choice: str = input(
            f"\n{name}, which game would you like to play?\n"
            "1. Rock, Paper, Scissors\n"
            "2. Guess the Number\n"
            "3. Quit\n"
        )

        if game_choice == "1":
            user_input: str = input(
                "👋 Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n"
            )

            player_input: int = int(user_input)

            rps_5.main(player_input)

        elif game_choice == "2":
            guess_number.main(name)

        elif game_choice == "3":
            print("\nGoodbye! 😊")
            break

        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Play Rock-Paper-Scissors or Guess the Number."
    )
    
    argument_name: str = "-n"
    argument_fullname: str = "--name"
    name_required: bool = True
    name_help: str = "Your first name"
    
    parser.add_argument(argument_name, argument_fullname, required=name_required, help=name_help)
    args = parser.parse_args()
    play_game(args.name)
