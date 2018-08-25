SODOKU
  Originally designed in C++ as a class project, I thought to try and create a sodoku solving algorithm
within Python. The jist of the algorithm is to find the cell on the board with the highest amount of 
illegal inputs, which means that it has the least amount of possibilities. Iterating through cells with
lower options means less backtracking when incorrect solutions are explored.
