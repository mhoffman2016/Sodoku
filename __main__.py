from __Board__ import Board

# Attempts to open the File given by the user
# filename = input("Enter file name:")
filename = ""
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
# Attempts to solve each Board
for board in boards:
    board.draw()
    board.solve()
    print("///////////")
    board.draw()
    print("Boards solved in %s calls" % board.calls)
    print("\n")
