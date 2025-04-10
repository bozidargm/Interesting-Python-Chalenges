def poker_hand_ranking(hand):
	cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
				'9':9, '10':10, 'J': 11, 'Q': 12, 'K':13, 'A':14}
	# List of hand's card numbers
	numbers = []

	for i in hand:
		numbers.append(cards[i[:-1]])
	
	numbers.sort()
	
	four = False
	three = False
	two_pair = False
	pair = False
	all_different = False
	straight = all(numbers[i+1]-numbers[i] == 1 for i in range(4)) 
	flush = all(hand[0][-1] == hand[i][-1] for i in range(5))
	pairs = []

	for i in numbers:
		if numbers.count(i) == 4:
			four = True
		elif numbers.count(i) == 3:
			three = True
		elif numbers.count(i) == 2:
			pairs.append(i)
		if len(pairs) == 2:
			pair = True
		elif len(pairs) == 4:
			two_pair = True
	
	if straight:
		if flush:
			if numbers[-1] == 14:
				return "Royal Flush"
			else:
				return "Straight Flush"
		else:
			return "Straight"
	elif flush and not straight:
		return "Flush"
	elif four:
		return "Four of a Kind"
	elif three and pair:
		return "Full House"
	elif three and not pair:
		return "Three of a Kind"
	elif two_pair:
		return "Two Pair"
	elif pair and not three:
		return "Pair"
	else:
		return "High Card"
