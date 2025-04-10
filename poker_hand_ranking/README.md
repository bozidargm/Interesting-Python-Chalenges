## The task

The task of this chelenge is to determine "poker-hand" value. The "hand" is passed to the function where it should be find out what cards we have.  

## The solution   

Basically, almost all the work is done by the conditions:  
1. Create a dictionary that will convert "hand carts" into numerical values, from 2 to Ace (14). That way, it's easy to tell if the cards are in a row.
2. Create list of hand cards values.
3. Create variables for all sort of combinations.
4. Iterate through list of card values: both numerical and suite mark to determin if all cards are of the same suit or not. Assign their value to appropriate variable.
5. Based on variable values determine with conditional which combination is in hand cards.