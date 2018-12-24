from Board import *
from SodokuWindow import *
import random

# fileToBoards: filename -> [Board]
# Takes a filename, attempts to open the file, then converts
# each line of the file into a game Board
def fileToBoards(filename):
    try:
        if filename == "":
            filename = "boards.txt"
        print("Using %s" % filename)
        file = open(filename)
    except:
        print('File not found in project directory')
        raise
    text = file.read()
    file.close()
    # Attempts to make a Board with each line
    splitText = text.split('\n')
    boards = []
    for count, line in enumerate(splitText):
        try:
            board = Board(line)
            boards.append(board)
        except:
            print("Line %s has improper format, exception during init" % count)
            raise
    return boards

# solveBoards: [Board] -> [Board]
# Takes a list of Boards and solves all of them
# Updates the user on the status of the process throughout
def solveBoards(boards):
    runningTotal = 0
    s = SodokuWindow()
    s.getMouse()
    for count, board in enumerate(boards, 1):
        board.draw()
        s.clear()
        s.updateBoard(board)
        s.getMouse()
        if not board.solve():
            raise Exception("Unsolveable Board!")
        s.updateMessage("Solved!")
        print("///////////")
        board.draw()
        print("Solved Board %s in %s calls" % (count, board.calls))
        runningTotal += board.calls
        print("Avg. = %s\n" % (runningTotal // (count)))
        s.getMouse()
    s.close()

# boardsToFile: [Board], filename -> file
# Takes a list of Boards and creates a file with the given name
def boardsToFile(boards, filename):
    file = open(filename, "w")
    for board in boards:
        file.write(board.matrixAsString())
        file.write("\n")

def main():
    # Attempts to open the File given by the user
    fileSource = input("Enter source file name:")
    fileDest = input("Enter destination file name:")
    boards = fileToBoards(fileSource)
    solveBoards(boards)
    if fileDest != "":
        boardsToFile(boards, fileDest)

main()