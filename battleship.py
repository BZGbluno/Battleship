

class BattleShip:

    def __init__(self, playerName, figure, boardSize=11):
        self.playerName = playerName
        self.boardSize = boardSize
        self.figure = figure
        self.boardSize = boardSize
        self.currTurn = 1

        self.board = []
        for i in range(boardSize):
            cols = []
            for j in range(boardSize):

                if i == 0 and j == 0:
                    cols.append("X")
                elif i == 0:
                    cols.append(str(j))
                elif j == 0:
                    cols.append(str(i))
                else:
                    cols.append("-")

            self.board.append(cols[:])

        self.attacks = []
        for i in range(boardSize):
            cols = []
            for j in range(boardSize):

                if i == 0 and j == 0:
                    cols.append("X")
                elif i == 0:
                    cols.append(str(j))
                elif j == 0:
                    cols.append(str(i))
                else:
                    cols.append("-")

            self.attacks.append(cols[:])

        # self.availableBoats = {4: 2, 3:2, 2: 3, 1: 4}
        self.availableBoats = {3:2}
        self.hits = 0
        for k in self.availableBoats:

            self.hits += self.availableBoats[k] * k

    def getTurn(self):
        return self.currTurn
    def addTurn(self):
        self.currTurn += 1

    def getName(self):
        return self.playerName

    def getAvailableBoats(self) -> list:
        return list(self.availableBoats)


    def isBoat(self, row, col):
        if self.board[row][col] == self.figure:
            return True
        return False


    def canAttack(self, row, col):
        if 0 <= row < len(self.attacks) and 0 <= col < len(self.attacks):
            if self.attacks[row][col] != "-":
                print("Previosly attacked here")
                return False
            return True
        else:
            print("Out of Bounds attack")
            return False
        
    def attack(self, row, col, miss=True):

        if miss == True:
            self.attacks[row][col] = "O"
        else:
            self.attacks[row][col] = "X"
            self.hits -= 1

            if self.hits == 0:
                self.printAttacks()
                return True

        self.printAttacks()
        return False



    def placeShip(self, startPos, boatSize, horizontal=True):
        if boatSize not in self.availableBoats:
            print(f"Boat Size not availble\nSelect one of the following: {self.getAvailableBoats()}")
            return False



        currBoard = self.board
        passed = True
        row, col = startPos

        # place the boat
        if horizontal:

            for i in range(boatSize):

                if 1 <= row < len(self.board) and 1 <= col < len(self.board[0]) and self.board[row][col] == "-":
                    currBoard[row][col] = self.figure
                    col += 1
                else:
                    passed = False
                    break
        else:
            for i in range(boatSize):

                if 1 <= row < len(self.board) and 1 <= col < len(self.board[0]) and self.board[row][col] == "-":
                    currBoard[row][col] = self.figure
                    row += 1
                else:
                    passed = False  
                    break

        if passed:
            self.board = currBoard
            self.availableBoats[boatSize] -= 1
            if self.availableBoats[boatSize] == 0:
                del self.availableBoats[boatSize]
        else:
            print("Not in bounds or ships collide: Please Retry\n")
            return

        self.printBoard()

    
    def _formatRow(self, row, width):
        return "".join(str(cell).center(width) for cell in row)

    def printBoard(self):

        width = max(len(str(self.boardSize - 1)), len(self.figure)) + 2

        print("\n\n")
        for row in self.board:
            print(self._formatRow(row, width))
        print("\n\n")

    def printAttacks(self):

        width = max(len(str(self.boardSize - 1)), 1) + 2

        print("\n")
        print("\t\t   Current Board")
        for row in self.attacks:
            print(self._formatRow(row, width))
    
    