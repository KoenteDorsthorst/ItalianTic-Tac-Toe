class Board:
    boardValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def drawBoard(self):
        for i in range(0, 9, 3):
            print(" " + self.boardValues[i] + " | " + self.boardValues[i + 1] + " | " + self.boardValues[i + 2] + " ")
            if i < 6:
                print("---|---|---")
