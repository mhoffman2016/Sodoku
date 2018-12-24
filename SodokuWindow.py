from graphics import *

class SodokuWindow(GraphWin):
    """ Graphical representation of the featured Board
    Attributes:
        featured - Board
            The Board to be drawn and used to update the graphic
        tiles - [[Text]]
            Matrix of all Text to appear on the featured Board
        message - Text
            String appearing below the board
    """
    def __init__(self, title="Sodoku",
                 width=240, height=240, autoflush=True):
        super().__init__(title, width, height*1.1, autoflush)
        self.featured = None
        origin = (5,5)
        boardWidth = width - origin[0]*2
        self.baseWidth = boardWidth / 9
        boardHeight = height - origin[1]*2
        self.baseHeight = boardHeight / 9
        # Draw the grid's horizontal lines
        for row in range(10):
            line = Line(Point(origin[0], row*self.baseHeight + origin[0]),
                        Point(boardWidth + origin[0], row*self.baseHeight + origin[0]))
            # Makes lines dividing blocks thicker
            if row%3 == 0:
                line.setWidth(3)
            line.draw(self)
        # Draw the grid's vertical lines
        for column in range(10):
            line = Line(Point(column*self.baseWidth + origin[0], origin[1]),
                        Point(column*self.baseWidth + origin[0], boardHeight + origin[1]))
            # Makes lines dividing blocks thicker
            if column%3 == 0:
                line.setWidth(3)
            line.draw(self)
        self.tiles = []
        for row in range(9):
            self.tiles.append([])
            for column in range(9):
                self.tiles[row].append(Text(Point(origin[0] + self.baseWidth/2 + self.baseHeight*column,
                                                  origin[1] + self.baseHeight/2 + self.baseHeight*row), ""))
                self.tiles[row][column].draw(self)
        self.message = Text(Point(width/2, height*1.04), "Click anywhere to start!")
        self.message.draw(self)

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
        self.updateMessage("New board!")

    # updateTile: self, int, int, int-> None
    # Called during solving of the Board to change specific tiles
    def updateTile(self, row, column, value):
        if value == 0:
            self.tiles[row][column].setText("")
        else:
            self.tiles[row][column].setText(value)

    # updateMessage: self, message -> None
    # Changes the message that appears at the bottom of the screen
    def updateMessage(self, message):
        self.message.setText(message)

    # addHighlight: self, row, column -> None
    # Places circles around the recently changed tiles
    # Removes pre-existing highlights
    def addHighlight(self, row, column):
        circle = Circle(Point(self.tiles[row][column].anchor.x,
                              self.tiles[row][column].anchor.y),
                              self.baseHeight/2)
        circle.draw(self)