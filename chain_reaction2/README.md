## The task

The task of this chelenge is to determine the minimum number of bombs that need to be set off for all bombs in 2D matrix to be destroyed by the chain reaction.

## The solution   

If the matrix contains "+" mines, all mines not separated by "0" fields will be activated by activating any mine in that group. So, it is necessary to determine the number of groups of mines that are connected to each other.  

It is similar if the matrix contains "x" mines, the difference is in the direction of activation of neighbor mines and in groups that do not have to be separated by "O" fields, but all mines from the group will be activated by activating any of them.  

1. Import numpy module since it is easier to access the elements of a 2D list if they are a numpy array.
2. Create hepler functions that will determine possible neighbor mines that can be activated by the mine passed to the function. "+" mines can activate neighboring mines if they are above, below, left or right of them, "x" mines can activate neighboring mines if they are diagonally from them.  
3. Create a numpy array from the input grid.  
4. Create set of all matrix cells.  
   - Matrix with "+" mines:  
         1. Iterating through matrix, looking for mines.  
         2. Creating list of neighboring cells under each iteration and looping through all neighbors looking for mines that can be activated. Count of groups of mines is incremented at the start of every cycle of iteration.  
   - Procedure for matrix with "x" mines is the same. At the end return count.