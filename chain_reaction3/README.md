## The task

The task of this chelenge is to determine the minimum number of bombs that need to be set off for all bombs in 2D matrix to be destroyed by the chain reaction. The difference compared to the previous challenge is that both "+" and "x" mines are present in the matrix at the same time.

## The solution  

The approach to solving this task is completely different from the previous one. Here we determine the groups of mines activated by each of the matrix mines, make all possible combinations of those groups and choose the combination with the smallest number of groups, which means the smallest number of mines that activate all the others.  

1. Import numpy for the most efficient looping through the matrix and combinations from itertools for the easiest creation of combinations of groups of mines that each mine of the matrix activates.  
2. Create two helper functions that determine the neighbor cells in relation to the passed one. Functions are separated for code clarity.
3. The main function starts by creating a numpy object from the input grid, creating a set of all cells of the matrix to check if the neighbors of the examined cells are inside the matrix, a set containing all the mines of the matrix and a list of mine groups activated by each of the matrix mines.
4. Iteration through the matrix: if the cell is a mine, determine all the mines it can activate and save the list of those mines for later determination of the best combination of those groups.
5. Making all possible combinations of mine groups.
6. Comparing each of the combinations of groups of activated mines (their union) with the set of all mines of the matrix.  
Since itertools.combinations sorts the combinations from the smallest number of elements (initially it gives only single elements) to the largest, the first combination found during the iteration contains the smallest number of groups (it means the smallest number of mines needed to create those groups) and this number is also the challenge solution.