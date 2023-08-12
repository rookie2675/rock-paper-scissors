import random
import os
from enum import Enum


class Move(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


def clear_screen():
    if os.name == 'nt':
        _ = os.system('clear')


def get_user_move():
    while True:
        try:
            user_input = int(input("Please choose one of the options above: "))
            return Move(user_input)
        except (ValueError, KeyError):
            print("Invalid input. Please choose 1, 2, or 3.")


def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "draw"
    elif (user_move, computer_move) in [(Move.Rock, Move.Scissors), (Move.Paper, Move.Rock), (Move.Scissors, Move.Paper)]:
        return "user"
    else:
        return "computer"


def play_game():
    while True:
        for data in Move:
            print(f'{data.value}. {data.name}')

        user_move = get_user_move()
        computer_move = random.choice(list(Move))

        print("\nYour choice:", user_move.name)
        print("Computer choice:", computer_move.name)

        result = determine_winner(user_move, computer_move)

        if result == "draw":
            print("The game has ended in a draw.")
        else:
            print("You won!" if result == "user" else "You lost")

        play_again = input("\nDo you wish to play again? [Y/N]: ")

        if play_again.upper() != 'Y':
            break

        clear_screen()


if __name__ == "__main__":
    play_game()
