import numpy as np
from itertools import combinations

def neighbors_plus(cell):
	"""
	Finding neighbors of "+" mine
	"""
	return [(cell[0]+1,cell[1]), (cell[0]-1,cell[1]), 
	      (cell[0],cell[1]+1), (cell[0],cell[1]-1)]

def neighbors_x(cell):
	"""
	Finding neighbors of "x" mine
	"""
	return [(cell[0]+1,cell[1]+1), (cell[0]+1,cell[1]-1), 
	      (cell[0]-1,cell[1]+1), (cell[0]-1,cell[1]-1)]

def min_bombs_needed(grid):
	matrix = np.array(grid)
	# Set of all matrix cells
	complete = set()
	# Set of matrix cells with mine
	mines = set()
	for i,j in np.ndenumerate(matrix):
		complete.add(i)
		if j == "+" or j == "x":
			mines.add(i)
	# Groups of mines activated by every mine of matrix
	groups = []

	# Iterating through matrix
	for cell,value in np.ndenumerate(matrix):
		# Set of all mines that can be activated by one of them
		neighbor_mines = []
		# Cells with mines that are activated by current cell in iteration
		checked = []
		temp_mines = []

		if cell in mines:
			# Appending first mine of matrix
			neighbor_mines.append(cell)
			# Looping until finding all mines that can be activated by
			# the firs in list of neighboring mines
			while neighbor_mines:
				if matrix[neighbor_mines[0][0], neighbor_mines[0][1]] == "+": 
					# List of neighbors of plus mines in matrix
					neighbor_mines_plus = [mine for mine in 
									neighbors_plus(neighbor_mines[0]) if mine in mines]
					for i in neighbor_mines_plus:
						if i not in neighbor_mines and i not in checked:
							neighbor_mines.append(i)
							checked.append(i)

				elif matrix[neighbor_mines[0][0], neighbor_mines[0][1]] == "x":
					# List of neighbors of x mines in matrix
					neighbor_mines_x = [mine for mine in 
										neighbors_x(neighbor_mines[0])	if mine in mines]
					for i in neighbor_mines_x:
						if i not in neighbor_mines and i not in checked:
							neighbor_mines.append(i)
							checked.append(i)
				# Adding examined mine to list
				temp_mines.append(neighbor_mines[0])
				del neighbor_mines[0]
		# Adding group of mines to list of groups
		if temp_mines:
			groups.append(temp_mines)


	# Creating set of groups subsets
	subsets = []
	groups2 = []
	# Removing doubles
	groups2 = [list(set(i)) for i in groups]
	for i in range(1, len(groups)+1):
		# Making combinations of groups
		for j in combinations(groups2,i):
			subsets.append(j)
	
	# Checking if any subset is the same
	# as set of all mines
	for i in subsets:
		subset = set()
		for j in i:
			for item in j:
				subset.add(item)
		# Lenght of subset is number of mines
		# that can activate all mines of matrix
		if subset == mines:
			return len(i)
	