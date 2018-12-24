class Board:
    """ Represents a Sodoku game Board
    Attributes:
        calls - int
            Keeps track of how often the 'solve' method is called
        matrix - [[int]]
            Stores all of the in-game digits
        conflicts - [[[boolean]]]
            Updated after placements, consulted in order to prevent illegal moves
        window - SodokuWindow
            Graphic showing the Board being solved in real-time
    """

    # __init__: self, String -> None
    # Takes a String and attempts to make a Board
    def __init__(self, seedString):
        self.calls = 0
        if len(seedString) != 81:
            raise Exception("seedString needs exactly 81 characters, contains "
                            + str(len(seedString)))
        # create a 3x9x9 Boolean list for storing number conflicts
        self.conflicts = []
        for i in range(3):
            self.conflicts.append([])
            for j in range(9):
                self.conflicts[i].append([])
                for k in range(9):
                    self.conflicts[i][j].append(False)
        # Store all values in the Matrix from the seedString,
        # and update all conflicts from those values
        self.matrix = []
        for row in range(9):
            self.matrix.append([])
            line = seedString[(row * 9):((1 + row) * 9)]
            for column, char in enumerate(line):
                self.matrix[row].append(0)
                value = int(char)
                if (value != 0):
                    if not self.checkConflicts(row, column, value):
                        self.updateCell(row, column, value, True)
                    else:
                        raise Exception("Illegal %s to be placed at (%s,%s)"
                                        % (value, row, column))

    # matrixAsString: self -> string
    # Creates a string of the game Board in the same format as the input for init
    def matrixAsString(self):
        string = ""
        for i in range(9):
            for j in range(9):
                string = string + str(self.matrix[i][j])
        return string

    # isSolved: self -> Boolean
    # Returns True if the Board is solved
    def isSolved(self):
        for i in range(9):
            for j in range(9):
                for k in range(1,10):
                    if self.matrix[i][j] == 0 or not self.checkConflicts(i,j,k):
                        return False
        return True

    # checkConflicts: self, int, int, int -> boolean
    # Returns whether the placement in question is illegal
    def checkConflicts(self, row, column, value):
        if (value < 1) or (value > 9):
            raise Exception("Out of Bounds! 'Value' is expected to be the same as the in-board digit")
        if self.conflicts[0][row][value - 1]:
            return True
        if self.conflicts[1][column][value - 1]:
            return True
        if self.conflicts[2][self.findBlock(row, column)][value - 1]:
            return True
        return False

    # updateCell: self, int, int, int, boolean -> None
    # Changes the matrix and conflict table to reflect the new value
    def updateCell(self, row, column, value, addingNumber):
        # Adding a number
        if addingNumber:
            if hasattr(self, "window"):
                self.window.updateTile(row, column, value)
            self.matrix[row][column] = value
            self.conflicts[0][row][value - 1] = True
            self.conflicts[1][column][value - 1] = True
            self.conflicts[2][self.findBlock(row, column)][value - 1] = True
        # Removing a number
        else:
            if hasattr(self, "window"):
                self.window.updateTile(row, column, 0)
            self.matrix[row][column] = 0
            self.conflicts[0][row][value - 1] = False
            self.conflicts[1][column][value - 1] = False
            self.conflicts[2][self.findBlock(row, column)][value - 1] = False

    # findBlock: self, int, int -> int
    # Returns the Block that the cell is located in
    # 0 is the top-left Block, 1 is top-center...
    def findBlock(self, row, column):
        return (row // 3) * 3 + (column // 3)

    # getPossibilites: self, int, int -> [int]
    # Returns the list of possible values for the cell
    def getPossibilites(self, row, column):
        possibilities = []
        for value in range(1, 10):
            if not self.checkConflicts(row, column, value):
                possibilities.append(value)
        return possibilities

    # findBestCell: self -> (int, int)
    # Returns the indices of the cell with the MOST conflicts
    def findBestCell(self):
        min = 9
        bestCell = None
        for row in range(9):
            for column in range(9):
                # if the cell is empty
                if self.matrix[row][column] == 0:
                    cur = len(self.getPossibilites(row, column))
                    if cur == 0:
                        return None
                    if min > cur:
                        min = cur
                        bestCell = (row, column)
        return bestCell

    # findUniqueCandidates: self -> [(int, int, int)]
    # Returns the index AND value of cells with only one possibility,
    #   considering the conflicts around them
    def findUniqueCandidates(self):
        uniqueCandidates = []
        # matrix of coordinates, first by block, then by number
        occurences = []
        for block in range(9):
            occurences.append([])
            for number in range(9):
                occurences[block].append([])
        for row in range(9):
            for column in range(9):
                # if the cell is empty
                if self.matrix[row][column] == 0:
                    possibilities = self.getPossibilites(row, column)
                    block = self.findBlock(row, column)
                    for number in possibilities:
                        occurences[block][number - 1].append((row, column))
        for block in occurences:
            for val, number in enumerate(block, 1):
                if len(number) == 1:
                    uniqueCandidates.append((number[0], val))
        return uniqueCandidates

    # solve: self -> Boolean
    # Attempts to solve the board, returns False if unsolveable
    # Uses recursion to attempt other possible solutions
    def solve(self):
        self.calls += 1
        if self.isSolved():
            return True
        # Begins with uniqueCandidate strategy
        uniqueCandidates = self.findUniqueCandidates()
        if len(uniqueCandidates) > 0:
            for uniqueCandidate in uniqueCandidates:
                self.updateCell(uniqueCandidate[0][0], uniqueCandidate[0][1], uniqueCandidate[1], True)
            if self.solve():
                return True
            else:
                for uniqueCandidate in uniqueCandidates:
                    self.updateCell(uniqueCandidate[0][0], uniqueCandidate[0][1], uniqueCandidate[1], False)
                return False
        # Begins finding next-best cells to attempt recursion
        bestCell = self.findBestCell()
        if bestCell == None:
            return False
        possibilities = self.getPossibilites(bestCell[0], bestCell[1])
        for value in possibilities:
            self.updateCell(bestCell[0], bestCell[1], value, True)
            if self.solve():
                return True
            else:
                self.updateCell(bestCell[0], bestCell[1], value, False)
        return False

    # draw: self -> None
    # Draws the current Board in the console
    def draw(self):
        for i in range(9):
            for j in range(9):
                if j in [3, 6]:
                    print("|", end="")
                cellChar = self.matrix[i][j]
                if cellChar == 0:
                    print (" ", end="")
                else:
                    print(cellChar, end="")
            if i in [2,5]:
                print("\n---+---+---")
            else:
                print("")
