## The task

The task of this chelenge is to determine whether all mines from 1D or 2D matrix will explode if starting from the first element of the matrix.  
To spice it up a bit, the task was extended to calculate "activation steps" - all mines activated by one mine make one step.  

## The solution  

1. Determining the dimensions of the matrix.
2. Creating a set of matrix cells.
3. Creating a set of neighbor cells. At the beginning it is the first cell of the matrix.
4. Looping through neighbor set: if the cell is "+" mine, we "activate" it by turning it into a number that also indicates the activation step, then we check if the top, bottom, left or right cell (if they are inside the matrix) are "+" or "x" mines and if so, we place them in the temp set. We do the same if the cell is "x" mine except we check if the diagonal cells are mines.
5. After iterating all the cells of the neighbor set, we start a new round of iterations with the cells of the temp set. We repeat this as long as there are mines in the neighborhood that we can activate.
6. Finally, we check if there is an unactivated mine in the matrix, if so, the function returns False, and if all mines are activated, the function returns True and the number of activation steps.

