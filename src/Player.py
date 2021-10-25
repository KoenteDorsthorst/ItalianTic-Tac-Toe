class Player:
    hasTurn = False

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    # Make slap button for JJ

    def playShape(self):
        print("hoi")

    def getName(self):
        return self.name

    def getHasTurn(self):
        return self.hasTurn

    def setHasTurn(self, set):
        self.hasTurn = set

    def getShape(self):
        return self.shape
