def overlapping_rectangles(rect1, rect2):
	# finding all coordinates for rect1 width
	x1 = []
	for i in range(rect1[0], (rect1[0]+rect1[2])):
	  x1.append(i)

	# finding all coordinates for rect2 width
	x2 = []
	for i in range(rect2[0], (rect2[0]+rect2[2])):
	  x2.append(i)

	# finding all coordinates for rect1 height
	y1 = []
	for i in range(rect1[1], (rect1[1]+rect1[3])):
	  y1.append(i)

	# finding all coordinates for rect2 height
	y2 = []
	for i in range(rect2[1], (rect2[1]+rect2[3])):
	  y2.append(i)

	# finding rectangles intersection x coordinates
	a = set(x1) & set(x2)

	# finding rectangles intersection y coordinates
	b = set(y1) & set(y2)

	# calculating overlapping area
	return (len(a))*(len(b))