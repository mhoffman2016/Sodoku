from __Board__ import *

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
    for line in splitText:
        boards.append(Board(line))
    return boards

# solveBoards: [Board] -> [Board]
# Takes a list of Boards and solves all of them
# Updates the user on the status of the process throughout
def solveBoards(boards):
    runningTotal = 0
    for count, board in enumerate(boards):
        board.draw()
        if not board.solve():
            raise Exception
        print("///////////")
        board.draw()
        print("Solved Board %s in %s calls" % (count, board.calls))
        runningTotal += board.calls
        print("Avg. = %s" % (runningTotal // (count + 1)))
        print("")

# boardsToFile: [Board], filename -> file
# Takes a list of Boards and creates a file with the given name
def boardsToFile(boards, filename):
    pass

# Attempts to open the File given by the user
filename = input("Enter file name:")
boards = fileToBoards(filename)
solveBoards(boards)
