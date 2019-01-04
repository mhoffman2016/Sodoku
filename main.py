from Board import *
from SudokuWindow import *
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

# solveBoards: [Board], Boolean, Boolean -> [Board]
# Takes a list of Boards and solves all of them
# Updates the user on the status of the process throughout
def solveBoards(boards, graphics=True, pause=False):
    runningTotal = 0
    if graphics:
        s = SudokuWindow()
        s.getMouse()
    for count, board in enumerate(boards, 1):
        board.draw()
        if graphics:
            s.clear()
            s.updateBoard(board)
            if pause:
                s.getMouse()
            s.updateMessage("Solving...")
        if not board.solve():
            raise Exception("Unsolveable Board!")
        if graphics:
            s.updateMessage("Solved!")
        print("///////////")
        board.draw()
        print("Solved Board %s in %s calls" % (count, board.calls))
        runningTotal += board.calls
        print("Avg. = %s\n" % (runningTotal // (count)))
        if graphics and pause:
            s.getMouse()
    if graphics:
        s.getMouse()
        s.close()

# boardsToFile: [Board], filename -> file
# Takes a list of Boards and creates a file with the given name
def boardsToFile(boards, filename):
    file = open(filename, "w")
    for board in boards:
        file.write(board.matrixAsString())
        file.write("\n")


# confirm: String -> Boolean
# Prints ONLY the String, then searches for a usable input
def confirm(message):
    entry = input(message)
    entry = entry.lower()
    if ("y" in entry) and not ("n" in entry):
        return True
    if ("n" in entry) and not ("y" in entry):
        return False
    else:
        print("Invalid input!")
        return confirm(message)


def main():
    # Attempts to open the File given by the user
    fileSource = input("Enter source file name:")
    boards = fileToBoards(fileSource)
    fileDest = ""
    if confirm("Output to file? Y/N:"):
        fileDest = input("Enter destination file name:")
    if confirm("Use graphics? Y/N:"):
        solveBoards(boards, True, confirm("Pause for clicks? Y/N:"))
    else:
        solveBoards(boards, False, False)
    if fileDest != "":
        boardsToFile(boards, fileDest)


main()