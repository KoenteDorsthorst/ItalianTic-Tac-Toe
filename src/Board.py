class Board:
    boardValues = [[" ", " ", " "],
                   [" ", " ", " "],
                   [" ", " ", " "]]
    boardWidth = 3
    boardHeight = 3

    def drawBoard(self):
        for i in range(0, len(self.boardValues)):
            print(f" {self.boardValues[i][0]} | {self.boardValues[i][1]} | {self.boardValues[i][2]} ")
            if i < self.boardHeight - 1:
                print("---|---|---")

    def isLegalMove(self, index1, index2):
        # Can only place a shape on an empty tile
        if self.boardValues[index1][index2] != " ":
            return False
        return True

    def getBoardValues(self):
        return self.boardValues

    def setBoardValues(self, value, index1, index2):
        self.boardValues[index1][index2] = value

    def hasWon(self, shape):
        for x in range(0, self.boardWidth):
            for y in range(0, self.boardHeight - 2):
                if self.boardValues[y][x] == shape and self.boardValues[y+1][x] == shape and self.boardValues[y+2][x] == shape:
                    return True

        for y in range(0, self.boardHeight):
            for x in range(0, self.boardWidth - 2):
                if self.boardValues[y][x] == shape and self.boardValues[y][x+1] == shape and self.boardValues[y][x+2] == shape:
                    return True

        for x in range(0, self.boardWidth - 2):
            for y in range(0, self.boardHeight - 2):
                if self.boardValues[x][y] == shape and self.boardValues[x+1][y+1] == shape and self.boardValues[x+2][y+2] == shape:
                    return True
                if self.boardValues[x][y+2] == shape and self.boardValues[x+1][y+1] == shape and self.boardValues[x+2][y] == shape:
                    return True

        return False

    def checkIfNextToTile(self, tile1, tile2):
        distance1 = abs(tile1[0] - tile2[0])
        distance2 = abs(tile1[1] - tile2[1])
        tileList = [tile1, tile2]
        for tile in tileList:
            if 0 < tile[0] < self.boardWidth - 1 and 0 < tile[1] < self.boardHeight - 1:
                return True
        if distance1 + distance2 <= 1:
            return True
        return False

        pass
