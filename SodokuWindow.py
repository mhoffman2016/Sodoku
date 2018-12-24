from graphics import *

class SodokuWindow(GraphWin):
    """ Graphical representation of the featured Board
    Attributes:
        featured - Board
            The Board to be drawn and used to update the graphic
        tiles - [[Text]]
            Matrix of all Text to appear on the featured Board
    """
    def __init__(self, title="Sodoku",
                 width=240, height=240, autoflush=True):
        super().__init__(title, width, height, autoflush)
        self.featured = None
        origin = (5,5)
        boardWidth = self.width - origin[0]*2
        baseWidth = boardWidth / 9
        boardHeight = self.height - origin[1]*2
        baseHeight = boardHeight / 9
        # Draw the grid's horizontal lines
        for row in range(10):
            Line(Point(origin[0], row*baseHeight + origin[0]),
                 Point(boardWidth + origin[0], row*baseHeight + origin[0])).draw(self)
            # Makes lines dividing squares thicker
            if row%3 == 0:
                Line(Point(origin[0], row*baseHeight + origin[0] - 1),
                     Point(boardWidth + origin[0], row*baseHeight + origin[0] - 1)).draw(self)
                Line(Point(origin[0], row*baseHeight + origin[0] + 1),
                     Point(boardWidth + origin[0], row*baseHeight + origin[0] + 1)).draw(self)
        # Draw the grid's vertical lines
        for column in range(10):
            Line(Point(column*baseWidth + origin[0], origin[1]),
                 Point(column*baseWidth + origin[0], boardHeight + origin[1])).draw(self)
            # Makes lines dividing squares thicker
            if column%3 == 0:
                Line(Point(column*baseWidth + origin[0] - 1, origin[1]),
                     Point(column*baseWidth + origin[0] - 1, boardHeight + origin[1])).draw(self)
                Line(Point(column*baseWidth + origin[0] + 1, origin[1]),
                     Point(column*baseWidth + origin[0] + 1, boardHeight + origin[1])).draw(self)

        self.tiles = []
        for row in range(9):
            self.tiles.append([])
            for column in range(9):
                self.tiles[row].append(Text(Point(origin[0] + baseWidth/2 + baseHeight*column,
                                                  origin[1] + baseHeight/2 + baseHeight*row), ""))
                self.tiles[row][column].draw(self)

    # clear: self -> None
    # Clears all text from the Window using the tiles matrix
    def clear(self):
        for row in self.tiles:
            for tile in row:
                tile.setText("")
                tile.setTextColor("black")

    # updateBoard: self -> None
    # Uses the featured Board to change the graphic, or uses the new one passed in
    def updateBoard(self, board=None):
        if board != None:
            self.featured = board
            board.window = self
        # if there was no board given and there's none featured yet...
        if self.featured == None:
            raise Exception("No Board is featured yet!")
        matrix = self.featured.matrix
        for row in range(9):
            for column in range(9):
                text = matrix[row][column]
                if text == 0:
                    continue
                self.tiles[row][column].setText(text)
                self.tiles[row][column].setTextColor("gray")

    # updateTile: self, row, column, value -> None
    # Called during solving of the Board to change specific tiles
    def updateTile(self, row, column, value):
        if value == 0:
            self.tiles[row][column].setText("")
        else:
            self.tiles[row][column].setText(value)