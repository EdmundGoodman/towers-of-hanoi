class GameBoard:
    def __init__(self, height):
        self.height = height
        self.reset()

    def reset(self):
        self.movesMade = 0
        self.board = [[i+1 for i in reversed(range(self.height))],[],[]]

    def isComplete(self, display=True):
        if display:
            print(self)

        return self.board[-1] == [i+1 for i in reversed(range(self.height))]

    def movepiece(self, fr, to, display=True):
        if display:
            print(self)
        self.movesMade += 1

        if len(self.board[fr]) != 0:
            piece = self.board[fr].pop()
        else:
            raise IndexError("Cannot remove piece from empty stack")

        if len(self.board[to]) == 0 or self.board[to][-1] > piece:
            self.board[to].append(piece)
        else:
            #self.board[to].append(piece)
            #print("Cannot place piece of higher magnitude to top of stack")
            raise Exception("Cannot place piece of higher magnitude to top of stack")

    def getStack(self, pos):
        return self.board[pos]

    def getStackHeight(self, pos):
        return len(self.board[pos])

    def peekStack(self, pos):
        return self.board[pos][-1]

    def __repr__(self):
        string = ""
        for y in reversed(range(self.height)):
            for x in range(3):
                try:
                    string += str(self.board[x][y]) + " "
                except IndexError:
                    string += "  "
            string += "\n"
        return string + "- - -"
