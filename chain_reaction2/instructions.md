## Chain Reaction (Part #2)  

As in the previous part, you will be given a rectangular array representing a "map" with three types of spaces:

    "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
    "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
    Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that need to be set off for all bombs to be destroyed by the chain reaction.**

Let's look at some examples:  
[  
>["+", "+", "+", "0", "+", "+", "+"],  
>["+", "+", "+", "0", "0", "+", "+"]  

]

For the map above, the answer is 2; to explode all bombs you just need to set off one "+" bomb in the right cluster and one in the left cluster.

[  
>["x", "0", "x"],  
>["x", "x", "x"]    

]

For the map above, the answer is 3; clearly setting off the three bottom "x" bombs is enough, and no less than three bombs suffice.

[  
>["x", "x", "x", "0", "x"],  
>["x", "x", "x", "x", "x"],  
>["x", "x", "x", "0", "x"]    

]

For the map above, the answer is 3; setting off the three rightmost bombs in the middle row will do the trick.
Examples

min_bombs_needed([  
>["+", "+", "+", "0", "+", "+", "+"],  
>["+", "+", "+", "0", "0", "+", "+"]   

]) ➞ 2

min_bombs_needed([  
>["x", "0", "x"],  
>["x", "x", "x"]  

]) ➞ 3

min_bombs_needed([  
>["x", "x", "x", "0", "x"],  
>["x", "x", "x", "x", "x"],  
>["x", "x", "x", "0", "x"]    

]) ➞ 3

Notes
- Note that both "+" and "x" bombs have an "explosion range" of 1.  
- To limit the difficulty, in this challenge each map will have only "+" or only "x"   bombs. The more challenging case of maps with both "+" and "x" bombs will be part 3!