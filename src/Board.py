class Board:

    boardValues = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    boardWidth = 3

    def drawBoard(self):
        for i in range(0, len(self.boardValues), self.boardWidth):
            print(f" {self.boardValues[i]} | {self.boardValues[i + 1]} | {self.boardValues[i + 2]} ")
            if i < 6:
                print("---|---|---")

    def isLegalMove(self, index):
        # Can only place a shape on an empty tile
        if self.boardValues[index] != " ":
            return False
        return True

    def getBoardValues(self):
        return self.boardValues

    def setBoardValues(self, value, index):
        self.boardValues[index] = value

