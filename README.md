SODOKU

The jist of the solving algorithm is to find the cell on the board with the highest amount of 
illegal inputs, which means that it has the least amount of possibilities. Iterating through cells with
lower options means less backtracking when incorrect solutions are explored.
