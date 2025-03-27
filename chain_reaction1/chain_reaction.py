def all_explode(grid):
	height = len(grid)
	width = len(grid[0])
	cell = grid[0][0]
	if cell == "0":
		return False
	# Set of all matrix coordinates
	complete = set()

	for i in range(height):
		for j in range(width):
			complete.add((i, j))

	count = 0
	neighbor_set = set()
	neighbor_set.add((0,0))

	while neighbor_set:
		temp_set = set()
		for i in neighbor_set:
			if grid[i[0]][i[1]] == "+":
				grid[i[0]][i[1]] = str(count + 1)
				# Finding possible bombs if matrix element is '+'
				possibe_bombs = [(i[0]+1,i[1]), (i[0]-1, i[1]), (i[0], i[1]+1), (i[0], i[1]-1)]
				for j in possibe_bombs:
					# Verifying that is in matrix and '0' or activated bomb
					if j in complete and not grid[j[0]][j[1]].isnumeric():
						temp_set.add(j) 
			elif grid[i[0]][i[1]] == "x":
				grid[i[0]][i[1]] = str(count + 1)
				# Finding possible bombs if matrix element is 'x'
				possibe_bombs = [(i[0]-1, i[1]-1), (i[0]-1, i[1]+1), (i[0]+1, i[1]-1), (i[0]+1, i[1]+1)]
				for j in possibe_bombs:
					# Verifying that is in matrix and '0' or activated bomb
					if j in complete and not grid[j[0]][j[1]].isnumeric():
						temp_set.add(j)

		neighbor_set = temp_set
		count += 1

	for i in grid:
		if "+" in i or "x" in i:
			return False
	return True, f"There are {count} steps of detonation"

print(all_explode(  
[  

 ["+", "+", "0", "+", "+", "+", "0"],
 ["0", "+", "+", "x", "0", "+", "x"]

]))
