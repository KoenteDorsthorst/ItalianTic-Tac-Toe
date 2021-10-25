from random import randint

from src.Board import Board
from src.Player import Player


# TODO
# Make minimum and maximum name length requirement

print("Welcome to Italian Tic-Tac-Toe")

name1 = input("Player 1 fill in your name: ")
shape1 = "X"
player1 = Player(name1, shape1)

name2 = input("Player 2 fill in your name: ")
shape2 = "O"
player2 = Player(name2, shape2)

players = [player1, player2]

print(f"Hello {players[0].getName()} and {players[1].getName()}")

board = Board()

gameIsPlaying = True


def randomizeTurnOrder():
    rand = randint(0, 1)
    players[rand].setHasTurn(True)


def giveTurnToNextPlayer():
    for i in range(0, len(players)):
        if players[i].getHasTurn():
            players[i].setHasTurn(False)
            if i == len(players) - 1:
                players[0].setHasTurn(True)
            else:
                players[i + 1].setHasTurn(True)
            break


def currentPlayer():
    for playerList in players:
        if playerList.getHasTurn():
            return playerList


randomizeTurnOrder()

while gameIsPlaying:
    # Turns to true when a valid move has been made
    moveMade = False

    player = currentPlayer()

    print(player.getName() + ", it's your turn!")

    board.drawBoard()
    playerMove = input()

    possibleInputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(0, len(possibleInputs)):
        if playerMove == possibleInputs[i]:
            if board.isLegalMove(i):
                moveMade = True
                board.setBoardValues(player.getShape(), i)


    if moveMade:
        giveTurnToNextPlayer()
    else:
        print("The move that has been made was not legal, try again")
