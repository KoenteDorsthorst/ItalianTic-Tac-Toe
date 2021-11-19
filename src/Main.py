import sys

from random import randint

from Board import Board
from Player import Player

# TODO Make minimum and maximum name length requirement

# TODO move this somewhere else
# All possible inputs for the player while playing the game
possibleInputs = [["a1", "a2", "a3"],
                    ["b1", "b2", "b3"],
                    ["c1", "c2", "c3"]]

print("Control the game by using the following inputs:")
print(sum(possibleInputs, []))

# How many turns each player has to do before the
turnsBeforeSliding = 6
turnCounter = 0

gameIsPlaying = True
gameLoop = True


# gives a random player a turn
def randomizeTurnOrder():
    rand = randint(0, len(players) - 1)
    players[rand].setHasTurn(True)


# Gives the turn to the next player in the player list
def giveTurnToNextPlayer():
    for i in range(0, len(players)):
        if players[i].getHasTurn():
            players[i].setHasTurn(False)
            if i == len(players) - 1:
                players[0].setHasTurn(True)
            else:
                players[i + 1].setHasTurn(True)
            break


# Returns the player that currently has the turn
def currentPlayer():
    for playerList in players:
        if playerList.getHasTurn():
            return playerList

# checks if the input that is given is correct
def isRealInput(input):

    for i in range(0, len(possibleInputs)):
        for n in range(0, len(possibleInputs[0])):

            if input == possibleInputs[i][n]:
                return True

    return False

# checks if the input that is given is correct
def getInputIndex(input):

    for i in range(0, len(possibleInputs)):
        for n in range(0, len(possibleInputs[0])):

            if input == possibleInputs[i][n]:
                return [i, n]

    # This should never happen, but is here for safety
    return [0, 0]


def get_input_with_interrupt(input_msg=None):
    try:
        if input_msg is not None:
            return input(input_msg)
        else:
            return input()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)


while gameLoop:

    print("Welcome to Italian Tic-Tac-Toe")

    name1 = get_input_with_interrupt("Player 1 fill in your name: ")
    shape1 = "X"
    player1 = Player(name1, shape1)

    name2 = get_input_with_interrupt("Player 2 fill in your name: ")
    shape2 = "O"
    player2 = Player(name2, shape2)

    players = [player1, player2]

    print(f"Hello {players[0].getName()} and {players[1].getName()}")

    board = Board()


    randomizeTurnOrder()

    while gameIsPlaying:
        # Turns to true when a valid move has been made
        moveMade = False

        player = currentPlayer()

        if turnCounter < turnsBeforeSliding:

            print(player.getName() + ", it's your turn!")

            board.drawBoard()
            playerMove = get_input_with_interrupt()

            # Places a shape on the location the user specified (if its available)

            for i in range(0, len(possibleInputs)):
                for n in range(0, len(possibleInputs[0])):
                    if playerMove == possibleInputs[i][n]:
                        if isRealInput(playerMove):
                            if board.isLegalMove(i, n):
                                moveMade = True
                                board.setBoardValues(player.getShape(), i, n)

        else:
            print(player.getName() + ", it's your turn!")
            board.drawBoard()
            movingShape = get_input_with_interrupt("Which shape do you want to move? ")
            movingLocation = get_input_with_interrupt("Where do you want to move the shape? ")

            # Check if inputs are valid
            if isRealInput(movingShape) and isRealInput(movingLocation):
                shapeIndex = getInputIndex(movingShape)
                locationIndex = getInputIndex(movingLocation)
                # Check if moving shape is the same as the players shape
                if board.getBoardValues()[shapeIndex[0]][shapeIndex[1]] == player.getShape():
                    # Check if location is empty
                    if board.getBoardValues()[locationIndex[0]][locationIndex[1]] == " ":
                        if board.checkIfNextToTile(shapeIndex, locationIndex):
                            board.setBoardValues(" ", shapeIndex[0], shapeIndex[1])
                            board.setBoardValues(player.getShape(), locationIndex[0], locationIndex[1])
                            moveMade = True

        if moveMade:
            if board.hasWon(player.getShape()):
                gameIsPlaying = False
            else:
                giveTurnToNextPlayer()
                turnCounter += 1
        else:
            print("The move that has been made was not legal, try again")

    board.drawBoard()
    print(f"Congratulation to {currentPlayer().getName()} for winning the game! Type \"restart\" to restart!")
    print("Type anything else to exit the program")
    restartInput = get_input_with_interrupt()
    if restartInput == "restart":
        board.resetBoard()
        gameIsPlaying = True
        turnCounter = 0
    else:
        gameLoop = False


