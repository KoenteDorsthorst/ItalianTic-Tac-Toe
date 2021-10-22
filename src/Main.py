from random import randint

from src.Board import Board
from src.Player import Player

print("Welcome to Italian Tic-Tac-Toe")

name1 = input("Player 1 fill in your name: ")
player1 = Player(name1)

name2 = input("Player 2 fill in your name: ")
player2 = Player(name2)

players = [player1, player2]

print("Hello " + players[0].getName() + " and " + players[1].getName())

board = Board()

gameIsPlaying = True


def randomizeTurnOrder():
    rand = randint(0, 1)
    players[rand].setHasTurn(True)


def currentPlayer():
    for player in players:
        if player.getHasTurn():
            return player


randomizeTurnOrder()

while gameIsPlaying:
    player = currentPlayer()

    print(player.getName() + ", it's your turn!")

    board.drawBoard()
    playerMove = input()



