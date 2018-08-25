class Board:
    # __init__: self, String -> void
    # Takes a String and attempts to make a Board
    def __init__(self, seedString):
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
                    self.updateCell(row, column, value, True)

    # solve: self -> Boolean
    # Attempts to solve the board, returns False if unsolveable
    # Uses recursion to attempt other possible solutions
    def solve(self):
        pass

    # isSolved: self -> Boolean
    # Returns True if the Board is solved
    def isSolved(self):
        pass

    # findBestCell: self, [(int, int)] -> (int, int)
    # Returns the indices of the cell with the MOST conflicts
    # Ignores cells in the given list
    def findBestCell(self, ignore=[]):
        maxConflicts = 0
        bestCell = None
        for row in range(0,9):
            for column in range(0,9):
                if self.matrix[row][column] == 0:
                    curConflicts = self.countConflicts(row, column)
                    if curConflicts > maxConflicts:
                        if (row, column) not in ignore:
                            bestCell = (row, column)
        return bestCell


    # updateCell: self, int, int, int, boolean -> void
    # Changes the matrix and conflict table to reflect the new value
    def updateCell(self, row, column, value, addingNumber):
        # Adding a number
        if addingNumber:
            self.matrix[row][column] = value
            self.conflicts[0][row][value - 1] = True
            self.conflicts[1][column][value - 1] = True
            self.conflicts[2][self.findSquare(row, column)][value - 1] = True
        # Removing a number
        else:
            self.matrix[row][column] = 0
            self.conflicts[0][row][value - 1] = False
            self.conflicts[1][column][value - 1] = False
            self.conflicts[2][self.findSquare(row, column)][value - 1] = False

    # countConflicts: self, int, int -> int
    # Returns the number of conflicts given the cell
    def countConflicts(self, row, column):
        count = 0
        for value in range(1, 10):
            if self.checkConflicts(row, column, value):
                count += 1
        return count

    # checkConflicts: self, int, int, int -> boolean
    # Returns whether the cell currently prevents the value
    def checkConflicts(self, row, column, value):
        if self.conflicts[0][row][value - 1]:
            return True
        elif self.conflicts[1][column][value - 1]:
            return True
        elif self.conflicts[2][self.findSquare(row, column)][value - 1]:
            return True
        return False

    # findSquare: self, int, int -> int
    # Returns the square that the cell is located in
    def findSquare(self, row, column):
        return (row // 3) * 3 + (column // 3)

    # draw: self -> void
    # Draws the current Board
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