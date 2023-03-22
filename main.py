import random
from enum import Enum


class Move(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


for data in Move:
    print(f'{data.value}. {data.name}')

userMove = None
while userMove is None:
    userInput = input("Please choose one of the options above: ")

    if userInput == "1":
        userMove = Move.Rock

    elif userInput == "2":
        userMove = Move.Paper

    elif userInput == "3":
        userMove = Move.Scissors
else:
    moves = list(Move)
    computerMove = random.choice(moves)

    print()
    print("Your choice: " + userMove.name)
    print("Computer choice: " + computerMove.name)

    wonMessage = "You won!"
    lossMessage = "You lost"

    if userMove == computerMove:
        print("The game has ended in a draw.")

    elif userMove == Move.Rock:
        if computerMove == Move.Scissors:
            print(wonMessage)
        elif computerMove == Move.Paper:
            print(lossMessage)

    elif userMove == Move.Paper:
        if computerMove == Move.Rock:
            print(wonMessage)
        elif userMove == Move.Scissors:
            print(lossMessage)

    elif userMove == Move.Scissors:
        if computerMove == Move.Paper:
            print(wonMessage)
        elif computerMove == Move.Rock:
            print(lossMessage)
