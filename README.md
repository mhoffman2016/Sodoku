SODOKU

This program displays Sodoku puzzles supplied by a text file being solved.

The program combines two strategies in order to solve the puzzles:

The first algorithm implemented considered cells which had the highest amount of conflicts,
meaning that they had the least amount of legal moves. The program would take this "best cell"
and iterate through each of its limited possibilities. Upon a dead end, the algorithm recurs,
and considers the next possibility for said cell. While possibly considered brute-force,
this strategy always uses the cell that will (theoretically) produce the least amount of
back-tracking. Essentially, the idea was to make well-educated guesses as to which decisions
would lead to the solution faster.

The second algorithm implemented, which now takes priority over the former, looks for "unique
candidates" on the board. "Unique candidates" are cells that, while having many legal moves,
have only one number possible **when considering the illegal moves around it**. Once you look
at the neighboring cells, it becomes apparent that only one cell in the block can host the
number in question, despite that individual cell being capable of many legal moves.
Credit to the link below for inspiration for this strategy, and a good example.
https://www.kristanix.com/sudokuepic/sudoku-solving-techniques.php
The algorithm finds every "unique candidate" available at any time, and places them all at once.
