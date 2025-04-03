import numpy as np

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
	for i,j in np.ndenumerate(matrix):
		complete.add(i)

	count = 0

	# If matrix is made of zeros and "+" mines
	if "+" in matrix:
		# Iterating through matrix
		for cell,value in np.ndenumerate(matrix):
			if value == "+":        
				count += 1
				matrix[cell[0], cell[1]] = "1"
				# List of neighbor mines, first mine found for start
				neighbor_mines = [cell]    

				# Looping until finding all mines that can be
				# acivated by first one in group 
				while neighbor_mines:
					neighbors = neighbors_plus(neighbor_mines[0])
					for i in neighbors:
						if i in complete and i not in neighbor_mines\
										and matrix[i[0], i[1]] == "+":
							neighbor_mines.append(i)
							matrix[i[0], i[1]] = "1"

					del neighbor_mines[0]

	# If matrix is made of zeros and "x" mines
	if "x" in matrix:
		# Iterating through matrix
		for cell,value in np.ndenumerate(matrix):
			if value == "x":
				count += 1
				matrix[cell[0], cell[1]] = "1"
				# List of neighbor mines, first mine found for start
				neighbor_mines = [cell] 

				# Looping until finding all mines that can be
				# acivated by first one in group
				while neighbor_mines:
					neighbors = neighbors_x(neighbor_mines[0])
					for i in neighbors:
						if i in complete  and i not in neighbor_mines\
										and matrix[i[0], i[1]] == "x":
							neighbor_mines.append(i)
							matrix[i[0], i[1]] = "1"
					del neighbor_mines[0]

	return count